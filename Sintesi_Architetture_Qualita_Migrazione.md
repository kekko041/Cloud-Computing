# Sintesi: Architetture Applicative, Qualità del Software e Migrazione/Consolidamento Infrastrutture

Sintesi mirata alle **Materie 4, 5 e 8** del bando AGID-01 (art. 7) — corrispondenti al **Ramo C** della [mappa mentale del concorso](Mappa_Mentale_AGID.html). Fonti: `AGID/Pubblicazioni_e_Linee_Guida_AGID.md` §4-5-8, `AGID/pdf/01`, `08-11`, `16-17`.

---

## 1. Modelli di Architetture Applicative e Sistemi IT (Materia 4)

*   **Piano Triennale 2024-2026, Parte 2 — Componenti tecnologiche** (`AGID/pdf/01`): il modello architetturale di riferimento della PA italiana è organizzato per componenti trasversali — **Servizi**, **Piattaforme**, **Dati e IA**, **Infrastrutture**, con la **Sicurezza** come livello trasversale a tutti gli strati (non un componente isolato).
*   **Sviluppo Sicuro / Secure by Design** (`AGID/pdf/08-11`), quattro allegati alle Linee Guida di sicurezza nello sviluppo applicazioni:
    *   **All. A — Ciclo di sviluppo software sicuro**: la sicurezza va integrata fin dalla fase di design (SDLC sicuro), non aggiunta a posteriori.
    *   **All. B — Sviluppo sicuro di codice**: pratiche di coding sicuro, prevenzione delle vulnerabilità più comuni.
    *   **All. C — Configurazione sicura del software di base**: hardening di sistemi operativi, middleware, container.
    *   **All. D — Modellazione delle minacce (Threat Modeling)**: identificazione dei rischi architetturali *prima* di scrivere codice (es. metodologia STRIDE).
*   **DevSecOps**: integrazione di controlli **SAST** (Static Application Security Testing, analisi statica del codice sorgente) e **DAST** (Dynamic Application Security Testing, test in esecuzione) nella pipeline CI/CD, in modo continuo e non episodico.
*   **OWASP Top 10**: riferimento per le vulnerabilità applicative più critiche da prevenire (Injection, Broken Authentication, ecc.), richiamato dalle stesse Linee Guida.

> **Collegamento con la materia 1**: gli standard di sicurezza applicativa (OAuth 2.0, mTLS, X.509) descritti nel ModI trovano qui la loro collocazione architetturale — sono controlli di sicurezza integrati nel ciclo di sviluppo secure-by-design.

---

## 2. Qualità e Metriche del Software (Materia 5)

*   **Modello di qualità ISO/IEC 25010**: framework di riferimento internazionale che scompone la qualità del software in caratteristiche misurabili — **funzionalità, affidabilità, usabilità, sicurezza, manutenibilità, portabilità** (oltre a efficienza prestazionale e compatibilità). È lo standard da citare quando si chiede di "valutare la qualità" di un sistema o di un capitolato di gara.
*   **Metriche operative**: function point (dimensionamento funzionale, utile per la stima economica in gara), densità dei difetti (bug/KLOC), code coverage dei test, tempo medio di remediation delle vulnerabilità (metrica di sicurezza operativa).
*   **Qualificazione CSP/SaaS per il Cloud della PA**: framework metodologico storicamente definito da AGID (`AGID/pdf/16-17`) per la due diligence su fornitori Cloud — criteri minimi di affidabilità, sicurezza, qualità del servizio. **Attenzione**: la competenza di qualificazione è stata **trasferita ad ACN** (Agenzia per la Cybersicurezza Nazionale) dal 2023 — in sede d'esame va citato il framework metodologico AGID ma attribuita correttamente la competenza attuale ad ACN.
*   **Manuale applicativo appalto pubblico di forniture ICT (v3.5)**: documento storico con i criteri di qualità dei beni/servizi ICT da inserire nei capitolati di gara — collega questa materia alla materia 9 (gare pubbliche ICT).

---

## 3. Metodologie di Migrazione e Consolidamento Infrastrutture (Materia 8)

*   **Principio Cloud First**: nella scelta del modello di servizio, l'ordine di preferenza è **SaaS > PaaS > IaaS** — si privilegia il livello di astrazione più alto compatibile con i requisiti, per minimizzare l'onere di gestione infrastrutturale della PA.
*   **Classificazione dei dati/servizi**: la normativa distingue tra dati/servizi **Ordinari, Critici e Strategici**. I servizi **Critici e Strategici** devono obbligatoriamente essere ospitati sul **Polo Strategico Nazionale (PSN)**, l'infrastruttura cloud sovrana della PA italiana.
    *   **Base normativa**: D.L. 77/2021 (conv. L. 108/2021), art. 33-septies, nell'ambito della governance PNRR; criteri di classificazione definiti da DPCM/circolari congiunte AGID-ACN-Dipartimento Trasformazione Digitale.
    *   **Governance/catena di comando**: indirizzo strategico della **Presidenza del Consiglio – Dipartimento per la Trasformazione Digitale** (Strategia Cloud Italia); requisiti di sicurezza e criteri di classificazione definiti con **ACN**; qualificazione dei cloud provider e Cloud Marketplace gestiti da **AGID**. La gara per la concessione è stata bandita da **Difesa Servizi S.p.A.** (in-house del Ministero della Difesa, per la rilevanza securitaria dell'infrastruttura), aggiudicata al consorzio **TIM (capofila) - CDP Equity - Sogei - Leonardo**, costituitosi in **PSN S.p.A.**: concessionario che progetta, realizza e gestisce i data center per 15 anni (2022-2037).
    *   **Attenzione in sede d'esame**: il PSN non è un ente pubblico né un'articolazione di AGID, ma un'infrastruttura privata in regime di concessione pubblica, sotto la vigilanza di sicurezza dell'ACN e gli indirizzi tecnici di AGID.
*   **Percorsi di migrazione** (`AGID/pdf/16-17`, Manuale/Kit di abilitazione al Cloud), in ordine crescente di complessità e beneficio cloud-native:
    1.  **Rehost** ("lift & shift"): spostamento dell'applicazione as-is su IaaS, minimo sforzo, minimo beneficio.
    2.  **Replatform**: modifiche minime per sfruttare servizi gestiti (es. passaggio a un DBaaS), beneficio intermedio.
    3.  **Rearchitect/Refactor**: riprogettazione cloud-native (microservizi, container, serverless), massimo sforzo, massimo beneficio (scalabilità, resilienza, costi operativi).
*   **Consolidamento dei data center della PA**: obiettivo strategico del Piano Triennale è la riduzione della frammentazione infrastrutturale storica (migliaia di piccoli data center locali) tramite migrazione verso il PSN o cloud qualificato.

> **Metodo per un caso gestionale di migrazione**: assessment applicativo → classificazione del dato/servizio (Ordinario/Critico/Strategico) → scelta del percorso (rehost/replatform/rearchitect) in base a vincoli di tempo/budget/rischio → revisione di sicurezza → metriche post-migrazione (ISO/IEC 25010 + KPI operativi).

---

## Mappa dei collegamenti con le altre materie del bando

| Materia 4-5-8 (questo documento) | Collegata a |
|---|---|
| OAuth 2.0, mTLS, X.509 nello sviluppo sicuro | Materia 1 — Normazione tecnica (ModI) |
| Qualificazione CSP/SaaS, criteri di qualità in gara | Materia 9/13 — Gare pubbliche ICT e Codice Appalti |
| Classificazione Critico/Strategico → PSN | Materia 7 — Programmazione e innovazione ICT (Piano Triennale) |
| TCO della migrazione cloud | Materia 10 — Formazione del budget |
