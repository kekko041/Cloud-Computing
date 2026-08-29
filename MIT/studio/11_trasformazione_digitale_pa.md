# Materia 11 — Trasformazione digitale della pubblica amministrazione
*Concorso MIT — Codice EPI (Specialista Informatico). Fonti: [`AGID_Sintesi_Preparazione_Concorso.md`](../../AGID_Sintesi_Preparazione_Concorso.md) §5-7-8, [`Sintesi_PM_Programmazione_Budget.md`](../../Sintesi_PM_Programmazione_Budget.md), [`Sintesi_Architetture_Qualita_Migrazione.md`](../../Sintesi_Architetture_Qualita_Migrazione.md), [`Sintesi_CAD_e_Appalti_ICT.md`](../../Sintesi_CAD_e_Appalti_ICT.md) §1-2, `AGID/pdf/01_Piano_Triennale_2024-2026_Agg2026.pdf`, `AGID/pdf/12_LG_Open_Data.pdf`, `AGID/Pubblicazioni_e_Linee_Guida_AGID.md` §4-8*

---

## 1. Il Piano Triennale per l'Informatica nella PA (2024-2026)

È lo strumento cardine della **governance strategica** della trasformazione digitale pubblica italiana, redatto da AGID su indirizzo del Dipartimento per la Trasformazione Digitale (DTD). Struttura in **tre parti** (`AGID/pdf/01`):

1. **Strategia** — visione, obiettivi e priorità di digitalizzazione del triennio.
2. **Tecnologie** (Componenti tecnologiche) — architettura di riferimento organizzata per componenti trasversali: **Servizi**, **Piattaforme**, **Dati e IA**, **Infrastrutture**, con la **Sicurezza** come livello trasversale a tutti gli strati (non un componente isolato).
3. **Strumenti** — modelli operativi e casi di buona pratica per attuare concretamente la strategia (es. **Strumento 1 — Approvvigionamento ICT**, che guida le PA nella scelta della procedura di gara più adatta).

### 1.1 I dieci principi guida del Piano Triennale

Concetto ricorrente trasversalmente in quasi tutte le materie del bando — da ricordare a memoria:

> **Digital & mobile first** · **Cloud first** · **API-first** · **Once Only** · **Data driven** · **Agile** · Servizi progettati sull'utente (*user-centered design*) · **Security & privacy by design** · **Riuso** · **Codice aperto (open source)**

### 1.2 KPI e monitoraggio

Il Piano Triennale definisce target misurabili di trasformazione digitale (es. percentuale di servizi migrati in cloud, adozione SPID, copertura PEC/domicilio digitale). Questi KPI sono lo strumento con cui si misura l'avanzamento della trasformazione digitale a livello di sistema-Paese, distinti dai KPI di singolo progetto (Materia gestione progettuale) ma coerenti con essi.

*Sintesi per l'esame*: quando un quesito chiede di "inquadrare normativamente" un intervento ICT nella PA, il Piano Triennale è quasi sempre il primo riferimento da citare, prima di scendere nel dettaglio tecnico specifico (CAD, Codice Appalti, singole Linee Guida).

---

## 2. Governance istituzionale della trasformazione digitale (PCM, DTD, AGID, ACN)

La trasformazione digitale della PA italiana è governata da tre soggetti distinti, tutti gravitanti attorno alla **Presidenza del Consiglio dei Ministri (PCM)**:

* **DTD (Dipartimento per la Trasformazione Digitale)**: incardinato **internamente** alla PCM (nessuna personalità giuridica propria, nessuna autonomia di bilancio), definisce la **strategia politica** e gestisce le risorse finanziarie strategiche (es. fondi digitali del PNRR).
* **AGID (Agenzia per l'Italia Digitale)**: **ente pubblico autonomo** con personalità giuridica propria, è il **braccio tecnico-operativo** sotto l'indirizzo politico del DTD. Redige materialmente il Piano Triennale ed emana le Linee Guida tecniche vincolanti (ModI, SPID, Cloud, sviluppo sicuro).
* **ACN (Agenzia per la Cybersicurezza Nazionale)**: ente pubblico autonomo sotto **controllo diretto** della PCM (per la delicatezza del mandato di sicurezza nazionale). Gestisce il **PSNC**, vigila sulla NIS2, certifica la sicurezza del Cloud per la PA (competenza di qualificazione CSP/SaaS **trasferita da AGID ad ACN nel 2023**) e gestisce lo **CSIRT Italia**.

| | Dipartimento (DTD) | Agenzia (AGID / ACN) |
|---|---|---|
| Personalità giuridica | No (parte della PCM) | Sì (ente autonomo) |
| Funzione | Indirizzo politico-strategico | Attuazione tecnico-operativa |
| Rapporto con PCM | Interno, gerarchico | Esterno, vigilanza |
| Bilancio | Nel bilancio PCM | Bilancio proprio |

*Sintesi pratica (Separation of Duties)*: il **DTD** decide la strategia e stanzia i fondi, l'**AGID** scrive le regole tecniche su come attuarla, l'**ACN** vigila sulla sicurezza dell'infrastruttura. Questa tripartizione è il modello di governance da citare ogni volta che un quesito riguarda "chi decide cosa" nella trasformazione digitale pubblica.

---

## 3. Cloud First e Strategia Cloud Italia

* **Principio Cloud First**: nella scelta del modello di servizio per una nuova iniziativa ICT, l'ordine di preferenza è **SaaS > PaaS > IaaS** — si privilegia il livello di astrazione più alto compatibile con i requisiti, per minimizzare l'onere di gestione infrastrutturale della PA.
* **Classificazione dei dati/servizi** (Strategia Cloud Italia, base normativa D.L. 77/2021 conv. L. 108/2021 art. 33-septies, criteri definiti da DPCM/circolari congiunte AGID-ACN-DTD):
  * **Ordinari**: compromissione senza danni significativi → possono restare su Public Cloud qualificato.
  * **Critici**: compromissione con danni rilevanti a funzioni istituzionali (es. anagrafe, sanità).
  * **Strategici**: essenziali per la sicurezza nazionale e funzioni core dello Stato.
  * I dati **Critici e Strategici** devono obbligatoriamente migrare sul **Polo Strategico Nazionale (PSN)**.
* **Il PSN**: non è un ente pubblico né un'articolazione AGID, ma un'**infrastruttura privata in regime di concessione pubblica** — gara bandita da Difesa Servizi S.p.A. (in-house Ministero della Difesa, per rilevanza securitaria), aggiudicata al consorzio TIM (capofila)-CDP Equity-Sogei-Leonardo, costituitosi in **PSN S.p.A.**, concessionario per 15 anni (2022-2037). Vigilanza di sicurezza ACN, indirizzi tecnici AGID.
* **Percorsi di migrazione** (Manuale/Kit di Abilitazione al Cloud, `AGID/pdf/16-17`), crescenti per complessità/beneficio:
  1. **Rehost** (lift & shift): spostamento as-is su IaaS, minimo sforzo/beneficio.
  2. **Replatform**: uso di servizi gestiti (es. DBaaS), beneficio intermedio.
  3. **Rearchitect/Refactor**: riprogettazione cloud-native (microservizi, container, serverless), massimo sforzo/beneficio.
* **Qualificazione CSP**: solo Cloud Service Provider accreditati (marketplace ACN) possono ospitare workload della PA.

*Sintesi per l'esame*: per un caso gestionale di migrazione, il metodo è: assessment applicativo → classificazione del dato/servizio (Ordinario/Critico/Strategico) → scelta del percorso (rehost/replatform/rearchitect) in base a vincoli di tempo/budget/rischio → revisione di sicurezza → metriche post-migrazione.

---

## 4. PNRR e digitalizzazione (Missione 1)

* Il **PNRR (Piano Nazionale di Ripresa e Resilienza)** finanzia gran parte della trasformazione digitale pubblica attraverso la **Missione 1 — Digitalizzazione, innovazione, competitività, cultura**, che include investimenti su identità digitale (SPID/CIE), interoperabilità (PDND), migrazione al cloud (PSN), competenze digitali della PA.
* **Rendicontazione a milestone/target**: i fondi PNRR sono erogati subordinatamente al raggiungimento di obiettivi quantitativi e temporali definiti (non a piè di lista) — da qui la centralità di **KPI misurabili** e di framework di project management strutturati (PRINCE2, PMBOK/PMP o Agile) nella gestione dei progetti ICT pubblici finanziati dal PNRR.
* Il mancato raggiungimento delle milestone comporta conseguenze finanziarie dirette (sospensione/decurtazione dei fondi), il che rende il **monitoraggio dell'esecuzione contrattuale** (Contract Monitoring) e la reportistica periodica elementi non accessori ma strutturali della gestione progettuale ICT pubblica.

---

## 5. Open data e riuso del software

* **Open Data by default** (art. 9 CAD): i dati pubblici non soggetti a restrizioni di privacy/sicurezza vanno pubblicati in **formati aperti e machine-readable** (CSV, JSON), descritti tramite ontologie condivise (es. **OntoPiA**) per garantirne la semantica interoperabile.
* **Licenze aperte**: coerentemente col principio "open by default" del CAD e con la **Direttiva UE Open Data 2019/1024**, i dataset pubblici vanno rilasciati con licenze come **CC BY 4.0** o l'equivalente italiana **IODL 2.0** (Linee Guida Open Data, `AGID/pdf/12`).
* **Riuso del software (artt. 68-69 CAD)**: prima di acquisire software proprietario, la PA deve valutare comparativamente open source → riuso da altra PA → sviluppo ex novo (da rilasciare poi in riuso) → proprietario. Le PA titolari di software sviluppato su specifiche proprie devono renderlo disponibile in riuso con licenza aperta.
* **Collegamento con l'e-procurement**: la logica "pubblica una volta, riusa ovunque" è la stessa che ispira il principio Once Only nelle gare pubbliche digitali (FVOE nel Codice Appalti).

---

## 6. Design dei servizi digitali: Designers Italia, UX/UI, accessibilità

* **Designers Italia**: iniziativa AGID che definisce **linee guida di design** per l'omogeneità visiva e funzionale dei servizi digitali pubblici (kit di interfaccia, pattern UX riutilizzabili, tono di voce), per garantire un'esperienza utente coerente su tutti i siti/app della PA.
* **User-centered design**: principio guida del Piano Triennale — i servizi digitali vanno progettati partendo dai bisogni reali dell'utente (cittadino/impresa), non dalla struttura organizzativa interna della PA erogatrice.
* **Accessibilità (WCAG 2.1/EN 301 549, Legge Stanca)**: requisito non negoziabile per ogni servizio digitale pubblico, trasversale al design (approfondito in [`10_normativa_amministrazione_digitale.md`](10_normativa_amministrazione_digitale.md) §5).
* **Amministrazione Trasparente (D.Lgs. 33/2013)**: obbligo di pubblicazione proattiva sui portali istituzionali di dati su bandi, appalti, bilanci, performance — la sezione `trasparenza.agid.gov.it` è un modello applicativo di riferimento citabile in un caso gestionale.

---

## 7. Formazione del budget e sostenibilità economica

* **Da "centro di costo" a "investimento"**: la spesa ICT pubblica va programmata secondo la logica del **TCO (Total Cost of Ownership)**, che include non solo il prezzo d'acquisto ma manutenzione, formazione, rischio di **lock-in** del fornitore, consumo energetico (**Green IT**).
* **Pareri di congruità tecnico-economica (art. 14-bis CAD)**: **non vincolante** per contratti sopra 1-2 M€ (l'amministrazione può procedere motivando anche con parere negativo); **vincolante** per acquisti tramite Consip/soggetti aggregatori su beni/servizi qualificati come strategici.
* I **Rapporti periodici sulla spesa ICT della PA** (`AGID/pdf/19-20`) forniscono dati di trend/benchmarking utili a motivare, in un caso gestionale, la sostenibilità economica di una scelta architetturale (es. TCO on-premise vs cloud).

---

## Domande di autoverifica

1. Quale ente **redige materialmente** il Piano Triennale per l'Informatica e ne emana le Linee Guida tecniche attuative?
   a) DTD
   b) AGID
   c) ACN
   d) Consip
   **Risposta: b)** — AGID è il braccio tecnico-operativo; il DTD definisce la strategia politica e i fondi.

2. Secondo la Strategia Cloud Italia, dove devono essere ospitati i dati classificati come "Critici" o "Strategici"?
   a) Su qualunque Public Cloud europeo
   b) Sul Polo Strategico Nazionale (PSN) o infrastrutture equivalenti ad altissima sicurezza
   c) Su infrastrutture on-premise obbligatoriamente
   d) Non esiste distinzione: tutti i dati PA seguono la stessa regola
   **Risposta: b)** — solo i dati Ordinari possono restare su Public Cloud qualificato; Critici e Strategici richiedono il PSN.

3. Qual è, tra i tre percorsi di migrazione al cloud, quello che offre il **massimo beneficio** (scalabilità, resilienza, riduzione costi operativi) a fronte del massimo sforzo?
   a) Rehost
   b) Replatform
   c) Rearchitect/Refactor
   d) Nessuno dei tre, la migrazione non produce mai benefici prestazionali
   **Risposta: c)** — la riprogettazione cloud-native (microservizi, container, serverless) è quella a massimo sforzo/massimo beneficio.

4. Il PSN (Polo Strategico Nazionale) è:
   a) Un ente pubblico interno ad AGID
   b) Un'infrastruttura privata in regime di concessione pubblica, vigilata da ACN
   c) Un dipartimento della Presidenza del Consiglio
   d) Un data center gestito direttamente dal Ministero dell'Economia
   **Risposta: b)** — concessionario privato (PSN S.p.A., consorzio TIM-CDP Equity-Sogei-Leonardo), non un ente pubblico.

5. Nel finanziamento PNRR dei progetti di trasformazione digitale, l'erogazione dei fondi è generalmente subordinata a:
   a) La semplice presentazione di un rendiconto di spesa a consuntivo
   b) Il raggiungimento di milestone/target quantitativi e temporali predefiniti
   c) Nessuna condizione, i fondi sono erogati a inizio progetto
   d) L'approvazione del solo Ministero dell'Economia, senza KPI
   **Risposta: b)** — la logica "a milestone" rende centrali KPI misurabili e monitoraggio contrattuale continuo.

6. Quale principio giustifica la richiesta che i software sviluppati ex novo da una PA vengano poi rilasciati in riuso con licenza aperta?
   a) Art. 3 CAD (diritto all'uso delle tecnologie)
   b) Artt. 68-69 CAD (acquisizione e riuso del software)
   c) Direttiva 2014/55/UE
   d) Regolamento eIDAS
   **Risposta: b)** — è la disciplina specifica su acquisizione/riuso software del CAD.
