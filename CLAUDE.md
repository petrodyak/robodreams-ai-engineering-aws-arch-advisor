# CLAUDE.md — aws-arch-advisor

## Хто я і що це

Я — Data Architect (AWS lakehouse: Datalake, Iceberg, Athena/Trino, Aurora, OpenSearch, Redshift, Step Functions).
Проходжу курс AI Engineering (RobotDreams, 2 потік). Цей репозиторій — мій наскрізний курсовий проєкт.

## Курсовий проєкт (4 етапи, одна система)

1. **Structured extraction** — витяг таблиць endpoints та service quotas з PDF AWS General Reference (по сервісах). Порівняння платної та локальної моделі. ← **поточний етап (ДЗ 1)**
2. **RAG** — пошук по AWS Prescriptive Guidance / Well-Architected PDF з відповідями, що цитують джерела, плюс тести якості.
3. **Агент** — багатокрокові задачі з інструментами (architecture review по AWS).
4. **Сервіс** — API, захист, моніторинг, облік витрат.

**Напрямок зафіксовано — не пропонуй його міняти.**
Якщо рішення на поточному етапі впливає на наступні (структура даних, імена файлів, формат JSON) — явно скажи про це.

## Обмеження

- Одна людина, 2 місяці, 3–4 год/тиждень. Мінімально достатні рішення, без over-engineering.
- **Стек:** Python 3.12, `uv` (не poetry, не pip-venv вручную), Anthropic (Claude) як єдина платна модель, Ollama з `qwen2.5:7b` як локальна. Не пропонуй OpenAI чи інші провайдери.
- Власних даних немає — тільки публічні.
- Бюджет на API — до $5 на все ДЗ 1. Перед масовими прогонами оціни вартість і скажи її.
- Ключі — тільки в `.env`; у Git — лише `.env.example`.

## Як працювати зі мною

- Українською, технічні терміни — англійською.
- **Я вчуся, а не збираю код.** Кожну зміну пояснюй: що робить цей шматок і чому саме так. Якщо є 2–3 варіанти — назви їх, порекомендуй один, поясни чому.
- Спочатку коротко суть, потім деталі. Без зайвих вступів.
- Перед написанням коду для нового кроку — покажи план і дочекайся мого «ок».
- Код: повні файли з шляхом у репозиторії, а не фрагменти без контексту.
- Не вигадуй API бібліотек — якщо не впевнений, перевір документацію або скажи, що не впевнений.
- Не роби `git commit` / `git push` без моєї явної команди.
- Не видаляй файли в `data/` — тільки переміщуй.
- Робота з Git (гілки, commits, PR, перевірки перед commit) — за правилами нижче. Перевірки запускаються `make check`.
> Git-правила (гілки, commits, PR, gates) — у `docs/GIT_RULES.md` репозиторію; у `CLAUDE.md` вони підключені через `@docs/GIT_RULES.md`.
 
## Структура репозиторію (цільова)
 
```
.
├── CLAUDE.md
├── GLOSSARY.md                  # терміни проєкту (Service Document, Quota Row, Neighbour Tail …)
├── .env.example                 # ANTHROPIC_API_KEY, OLLAMA_HOST
├── .gitignore                   # .env, .venv, data/source/, data/pool/*.pdf, data/raw/*.pdf
├── README.md                    # проблема, користувач, 4 етапи, як запустити, як відтворити дані
├── REPORT.md                    # звіт-порівняння по ДЗ 1
├── Makefile                     # make run — запуск одною командою
├── pyproject.toml               # uv
├── main.py                      # точка входу ДЗ 1
├── prompts/                     # промпти з версіями
│   ├── CHANGELOG.md
│   ├── extract_v1.txt
│   └── extract_v2.txt
├── config/
│   └── sampling.yaml            # конфігурації temperature/top_p
├── data/
│   ├── source/                  # aws-general-endpoints-and-quotas.pdf (25 МБ, не в Git)
│   ├── pool/                    # УСІ 100 PDF (не в Git) + manifest.csv, profile.csv (у Git)
│   ├── raw/                     # 30 відібраних: *.pdf (не в Git) + *.txt + manifest.csv (у Git)
│   └── gold/                    # 10 JSON golden set (у Git)
├── results/                     # виходи моделей: JSONL по прогонах + metrics (у Git)
├── scripts/
│   ├── split_pdf.py             # source → pool за закладками PDF
│   ├── select_docs.py           # pool → raw за data/raw/manifest.csv
│   └── extract_text.py          # raw/*.pdf → raw/*.txt
├── src/
│   ├── extract/                 # етап 1: schema.py, llm/ (спільний інтерфейс), pipeline.py, metrics.py
│   ├── rag/                     # етап 2
│   ├── agent/                   # етап 3
│   └── api/                     # етап 4
├── evals/
├── tests/
└── docs/
    ├── GIT_RULES.md             # гілки, commits, PR, gates (make check)
    ├── stage1-data-contract.md  # контракт даних етапу 1 — звіряти код із ним
    └── adr/                     # 0001 standard quota tables only, 0002 model extracts / code derives
```
 
## ДЗ 1 — «Structured Extraction Service» (30 балів, дедлайн 27.10 23:59)

Сервіс, що витягує структуровані дані з «брудних» текстів за схемою, порівнює провайдерську (Claude) і локальну (qwen2.5:7b) моделі й обґрунтовує вибір для продакшну цифрами.

### Дані

- Джерело: 100 PDF по сервісах із AWS General Reference (`data/pool/`).
- Робочий набір: **30 документів** у `data/raw/`, відібрані за трьома групами (список — у `data/raw/manifest.csv`, колонка `group`):
  - `short` (~10): 1–2 стор., endpoints + кілька quotas — база для локальної 7B-моделі;
  - `medium` (~10): 3–6 стор., кілька таблиць quotas — тут видно різницю промптів;
  - `edge` (~10): довгі / FIPS / dual-stack / footnotes / без quotas — для розбору помилок.
- Документи 20+ стор. (EC2, S3, IAM) у ДЗ 1 не беремо — не влізуть у контекст локальної моделі.
- «Брудність» наших даних: різна довжина, пропущені поля (немає quotas, «Not supported», «—»), шум PDF-екстракції (зламані колонки, перенесені рядки, зшиті комірки, футноти, колонтитули). Друкарських помилок і змішаних мов немає — так і пишемо в README.
- **Golden set: 10 із 30** (3–4 з кожної групи) у `data/gold/`. Підхід: модель робить чернітку JSON → я вручну звіряю з PDF і правлю (model-assisted, human-verified) — так і документуємо.
- Імена файлів і формат JSON фіксуємо зараз: `raw/*.txt` і `gold/*.json` далі йдуть у RAG (етап 2) і в агента (етап 3).

### Кроки

1. **Схема + baseline-промпт** (заняття 3) — Pydantic-схема: ≥6 полів, ≥1 enum, ≥1 вкладений об'єкт/список. Baseline-промпт, Claude через API зі structured output, retry + timeout, прогнати всі 30, зберегти в `results/`.
2. **Друга модель + заміри** (заняття 2–3) — qwen2.5:7b через Ollama **через спільний інтерфейс** з Claude. Семплінг (temperature, top_p) у конфіг, ≥2 конфігурації. Для кожної моделі: точність по полях на golden set, % валідних відповідей, latency p50/p95, вартість на 1000 документів.
3. **Версіонування промптів і валідація** (заняття 4) — промпти в окремих файлах з версією і CHANGELOG (≥2 версії, що змінили і чому). Валідація кожної відповіді за схемою; невалідна → одна спроба виправлення → `failed`. До кожного результату логувати модель, версію промпту, параметри семплінгу.
4. **REPORT.md** (після Q&A 26.10) — таблиця «модель × версія промпту × семплінг» з усіма метриками; розбір 3–5 характерних помилок (що замість чого і чому); фінальний вибір для продакшну в 1 абзац + за яких умов змінив би рішення.

Stretch (без балів, тільки якщо лишиться час): третя дешева модель, регресійний прогін промптів на golden set, кеш відповідей.

### Терміни

| Дата | Що |
|---|---|
| 24.10 | Чекпоінт: кроки 1–2 в репо, посилання в чат `#ai-engineering-2-flood` (без балів) |
| 26.10 | Q&A: фідбек на чекпоінт |
| 27.10 23:59 | Дедлайн: кроки 1–4 |

### Критерії (30 балів)

- Крок 1 — 6: схема за вимогами (2), structured output + retry/timeout (2), усі тексти прогнані й збережені (2)
- Крок 2 — 8: локальна модель через спільний інтерфейс (3), семплінг у конфігу + ≥2 конфігурації (2), коректні заміри (3)
- Крок 3 — 8: ≥2 версії промпту з changelog (3), валідація + обробка невалідних (3), логування моделі/версії/параметрів (2)
- Крок 4 — 6: таблиця з метриками (2), розбір 3–5 помилок (2), обґрунтований вибір (2)
- Якість репо — 2: README, запуск однією командою, ключі не в коді

Найбільше балів — за кроки 2 і 3. Не потрібно: UI, деплой, fine-tuning, великий датасет, ідеальна точність.

### Технічні вимоги

- Python 3.11+ (у нас 3.12), запуск однією командою (`make run` або `python main.py`).
- Локальна модель має працювати на звичайному ноутбуці.
- Здача — одне посилання на GitHub-репозиторій: https://github.com/petrodyak/robodreams-ai-engineering-aws-arch-advisor

### Що має бути в репозиторії
- код сервісу та схема;
- папка prompts/ з версіями та changelog;
- data/ з текстами та golden set;
- results/ з виходами моделей;
- REPORT.md із звітом-порівнянням;
- README.md: як запустити і що потрібно встановити.

## Поточний стан і наступний крок

### Зроблено (15.10, дані)
- `data/pool/` — усі 100 PDF + `manifest.csv` + `profile.csv` (слова, endpoint-рядки, FIPS/dual-stack/quotas-маркери по кожному файлу).
- `data/raw/manifest.csv` — 30 відібраних: колонки `file, service, group (short|medium|edge), gold (1 = у golden set), priority, pages, words, endpoint_rows, note`. Усі 16 `priority=1` сервісів усередині.
- `scripts/select_docs.py` — копіює 30 PDF з `pool/` у `raw/` за manifest. Запущено, 30 PDF лежать у `raw/`.
- `scripts/split_pdf.py` тепер пише в `pool/`; `.gitignore` і README оновлені.
- Групи ділили **за словами, а не сторінками** (таблиці рідкі: 4 стор. = 489 слів, 39 стор. = 4 020 слів; діапазон 0.5k–5k слів ≈ 0.7k–8k токенів — усе влазить у контекст qwen2.5:7b).

### Зроблено (15.10, проєкт і дизайн схеми)
- `pyproject.toml` + `uv.lock` (`anthropic`, `ollama`, `pydantic`, `pypdf`, `python-dotenv`, `pyyaml`; dev: `pytest`, `ruff`), `.python-version = 3.12`. Нові залежності — тільки через `uv add`, не руками.
- `Makefile`: `install` (uv sync), `data` (split + select), `text` (extract), `check` (ruff check + ruff format --check + pytest). Цілі `run` ще немає — з'явиться разом з `main.py`.
- `scripts/extract_text.py` — `pypdf` layout mode, 30 `.txt` у `data/raw/`. Текст не чистимо; єдина зміна — лігатури `ﬀ ﬁ ﬂ ﬃ ﬄ` → звичайні літери (рішення прийнято). Сторінки розділені `\f`.
- Крок 0 Git: `docs/GIT_RULES.md`, pre-commit gates через `make check`, PR #1 змерджено.
- Design interview → `GLOSSARY.md`, `docs/stage1-data-contract.md` (10 пунктів контракту), ADR-0001 і ADR-0002. **Схема етапу 1 спроєктована — код пишемо за контрактом, а не придумуємо заново:**
  - `ServiceDocument`: `schema_version: Literal["1"]`, `service`, `quota_table_format: standard | non_standard | none`, `endpoints: list[EndpointRow]`, `quotas: list[QuotaRow]`.
  - `EndpointRow`: `region_name, region_code, endpoint, protocol (HTTPS|HTTP)` — тільки друковані колонки; `endpoint_type (fips|dual_stack|ipv4|global)` — computed field з hostname, у метриках точності не рахується.
  - `QuotaRow`: `name, default: str (як надруковано), adjustable: bool, description` — тільки зі Standard Quota Table (`Name | Default | Adjustable | Description`); інші формати → `quotas: []` + `quota_table_format = non_standard` (ADR-0001).
  - Модель витягує лише надруковане; парсинг `default` у число/scope — у коді, пізніше (ADR-0002). Мультирегіональні `default` → `"us-east-1: 20,000; us-east-2: 6,000"`.
  - Валідатор на кожному `str`: `" ".join(s.split())`, більше нічого. `service` не збігся з manifest → validation failure (детектор Neighbour Tail).
  - Golden set: чернетка з прогону `claude__v1__t0` → `data/gold/<name>.json` → ручна правка по PDF.

### Відомі особливості даних (зафіксовані рішення)
- **Хвости сусідніх сервісів лишаємо як є.** Розрізання по закладках іде посторінково, тому перша сторінка файлу містить кінець попереднього сервісу (напр. у `006-aurora-dsql` — шматок quotas від Aurora), а власні quotas можуть витікати в наступний файл. Промпт має витягати тільки цільовий сервіс; у golden set — тільки дані цільового сервісу.
- Пропущені поля є природно: без quotas-таблиці (`007`, `042`, `047`), «N/A» (`047`, `048`), глобальні сервіси з 3 endpoint-рядками (`010`, `074`).
- Текст із PDF брудний: ламані слова (`ap-\nsoutheast-4`), колонтитули «AWS General Reference … Version 1.0 NNN». Лігатури вже нормалізовані в `.txt`.
- `093-aws-services.pdf` — не сервіс (зведений список), виключено.

### Наступний крок (Claude Code)
1. `src/extract/schema.py` — Pydantic-схема за `docs/stage1-data-contract.md` (поля вище) + unit-тести на валідатори (whitespace, `endpoint_type`, перевірка `service`). План полів уже є — показати лише план файлу/тестів і чекати «ок».
2. `src/extract/llm/` — спільний інтерфейс для Claude і Ollama (одна функція `extract(text, service, prompt, sampling) -> ServiceDocument | failed`), спочатку тільки Claude-реалізація зі structured output, retry + timeout.
3. `prompts/extract_v1.txt` + `prompts/CHANGELOG.md`, `config/sampling.yaml` (перша конфігурація `t0`), `main.py` + ціль `make run`; оцінити вартість, прогнати 30 → `results/claude__v1__t0.jsonl` з логуванням моделі/версії промпту/семплінгу.
4. Golden set: з результатів п.3 скопіювати 10 файлів `gold=1` у `data/gold/` → я звіряю вручну з PDF.
5. Далі крок 2 ДЗ: Ollama-реалізація того ж інтерфейсу, друга конфігурація семплінгу, `metrics.py`.
