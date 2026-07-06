# Intelligenza Artificiale e AI Act
*(Focus per il concorso Esperto ICT - Banca d'Italia)*

L'adozione dell'Intelligenza Artificiale nel settore bancario e istituzionale non è più solo un'opportunità di ottimizzazione, ma una sfida complessa di **Governance, Sicurezza e Conformità Normativa**. Nel contesto della Banca d'Italia, l'IA deve essere governata attraverso un approccio strutturato che bilanci l'innovazione tecnologica con la mitigazione dei rischi sistemici.

---

## PARTE 1: L'AI Act (Regolamento UE 2024/1689)
L'AI Act è il primo framework normativo europeo organico sull'IA, basato su un **approccio orientato al rischio (Risk-based approach)**.

### 1. Classificazione del Rischio
L'AI Act divide i sistemi in quattro categorie di rischio. Per una Banca Centrale, le attenzioni si concentrano sui sistemi **Ad Alto Rischio (High-Risk)**, che includono:
* **Valutazione del merito creditizio (Credit Scoring):** Algoritmi che decidono l'affidabilità creditizia dei cittadini/imprese.
* **Biometria e Sicurezza:** Sistemi di identificazione biometrica remota per l'accesso a infrastrutture critiche.
* **Gestione Algoritmica dei Lavoratori (Capo IX):** Sistemi IA utilizzati per monitorare, valutare o organizzare il lavoro dei dipendenti (tema delicatissimo dal punto di vista giuslavorista e della privacy).

### 2. Obblighi per i Sistemi ad Alto Rischio
Se la Banca d'Italia sviluppa o implementa internamente ("Deployer" o "Provider") un sistema ad alto rischio, deve garantire:
* **Sorveglianza Umana (Human-in-the-Loop):** Le decisioni critiche prese dall'IA devono poter essere comprese, interrotte e sovrascritte da un operatore umano qualificato.
* **Data Governance e Assenza di Bias:** I set di dati di addestramento (Training Data) devono essere pertinenti, rappresentativi ed esenti da errori o bias discriminatori.
* **Tracciabilità (Logging) e Trasparenza:** Ogni output deve essere ripercorribile per dimostrare come il sistema sia giunto a una determinata conclusione (Explainable AI - XAI), fondamentale in caso di audit di vigilanza.

### 3. Le Autorità di Sorveglianza in Italia
La **Legge 23 settembre 2025, n. 132** ha recepito l'art. 70 dell'AI Act designando un modello **duale** di autorità nazionali competenti:
* **AgID (Agenzia per l'Italia Digitale):** autorità di notifica e autorità di vigilanza del mercato per la generalità dei sistemi IA.
* **ACN (Agenzia per la Cybersicurezza Nazionale):** autorità di vigilanza del mercato per i sistemi IA impiegati in ambiti di sicurezza nazionale e cybersicurezza.

Le autorità di vigilanza settoriali **mantengono le proprie competenze specifiche** e operano in raccordo con AgID/ACN: **Banca d'Italia** e **CONSOB** restano competenti sui sistemi IA ad alto rischio nel settore finanziario/creditizio (es. credit scoring), mentre il **Garante Privacy** resta competente sui profili di trattamento dati personali (GDPR). A livello UE, il coordinamento complessivo è affidato all'**AI Office** della Commissione Europea.

### 4. NIST AI RMF (AI Risk Management Framework)
Framework pubblicato dal NIST (USA, versione **AI RMF 1.0**, gennaio 2023), **volontario e non certificabile** — a differenza dell'AI Act (vincolante) e di ISO/IEC 42001 (certificabile da terze parti). Rappresenta il livello di **Risk-Management Operating Model**: la metodologia interna per identificare, misurare e trattare i rischi IA lungo tutto il ciclo di vita del sistema.

Si articola in 4 funzioni core:
* **Govern:** cultura, policy e responsabilità per la gestione del rischio IA (trasversale alle altre tre funzioni).
* **Map:** contestualizza il sistema IA, individuandone scopo, requisiti e impatti previsti nello specifico contesto d'uso (es. sotto-funzione **Map 1.1**, "caratterizzazione del sistema").
* **Measure:** misura e monitora i rischi identificati con metriche quantitative/qualitative (bias, robustezza, sicurezza).
* **Manage:** alloca le risorse per trattare i rischi (mitigazione, trasferimento, accettazione) con piani di miglioramento continuo.

**Strategia "Single Spine of Controls":** un unico controllo tecnico ben progettato (es. "Documentazione Tecnica del Modello") può soddisfare contemporaneamente più framework — es. **AI Act Annex IV** (trasparenza), **ISO 42001 Annex A.6** (ciclo di vita AIMS) e **NIST AI RMF Map 1.1** (caratterizzazione del sistema) — riducendo la ridondanza di compliance.

---

## PARTE 2: Vulnerabilità Tecniche dell'IA Generativa e Agentica
Oltre alla conformità normativa, l'uso di Large Language Models (LLM) o di Agenti Autonomi introduce nuove superfici di attacco, come evidenziato dal framework **SANS AI Security Maturity Model (AI-SMM)** e dalle classificazioni OWASP per LLM.

### 0. SANS AI Security Maturity Model (AI-SMM)
Framework di SANS, compagno operativo del "SANS Secure AI Blueprint", allineato a NIST AI RMF, AI Act, ISO 42001 e OWASP AI Exchange/Agentic Top 10. Valuta la maturità IA lungo **3 pilastri indipendenti** (un'organizzazione può trovarsi a stadi diversi su ciascuno):
* **Protect** (*AI for Security*): protezione delle implementazioni IA da attacchi avversari (data poisoning, prompt injection, model theft), inclusa la gestione delle Non-Human Identity (NHI) negli stadi avanzati.
* **Utilize** (*AI for Security*): uso dell'IA per rafforzare la sicurezza (detection, risposta automatizzata, threat hunting).
* **Govern** (*AI for Compliance*): policy, risk management e supervisione che abilitano e vincolano gli altri due pilastri.

**I 5 stadi di maturità:**
1. **Unaware/Ad Hoc**: nessun approccio formale, uso di IA pubblica senza supervisione (BYOAI).
2. **Reactive/Policy-Emerging**: policy di base (spesso "non usare l'IA"), nessuna metrica.
3. **Defined/Risk-Informed**: governance formale cross-funzionale, rischi IA tracciati; da qui è obbligatoria la gestione NHI e un owner umano per ogni agente.
4. **Managed/Integrated**: maturità quantitativa, IA integrata nelle operazioni di sicurezza con esiti misurabili.
5. **Optimizing/Adaptive**: frontiera "AI-native", difese adattive e auto-migliorantesi.

Per un'istituzione finanziaria regolata come Banca d'Italia, gli **Stadi 3-4** rappresentano il riferimento realistico (non necessariamente lo Stadio 5).

**Regole di calcolo del punteggio complessivo:**
* **Governance Floor Rule**: la maturità complessiva non può superare di più di uno stadio il pilastro Govern.
* **Minimum Pillar Rule**: la maturità complessiva non può superare di più di uno stadio il pilastro più basso dei tre.

**Concetti da ricordare:** il **Principle of Least Agency** (analogo agentico del Least Privilege: verificare che l'autonomia di un agente sia realmente necessaria prima di concederla) e la distinzione **BYOAI vs Shadow AI** (Shadow AI esiste solo se viola una policy già stabilita, quindi possibile solo dallo Stadio 2 in poi).

### 1. Attacchi ai Modelli Generativi
* **Prompt Injection (Iniezione di Prompt):** L'attaccante inserisce comandi nascosti nel testo di input per costringere il modello a ignorare le proprie istruzioni di sistema (System Prompt) e a compiere azioni malevole (es. esfiltrare dati sensibili presenti nel contesto).
* **Jailbreaking:** Tecniche di ingegneria sociale applicate al prompt per bypassare le restrizioni etiche o di sicurezza del modello (es. "Rispondi come se fossi in modalità sviluppatore senza filtri").
* **Data Poisoning (Avvelenamento dei Dati):** Negli scenari in cui la banca effettua il *fine-tuning* di un modello, un attaccante potrebbe manipolare i dati di addestramento (es. inquinare un repository di log) per inserire vulnerabilità dormienti (backdoor).

### 2. Rischi dei Sistemi Agentici (Autonomous Agents)
Gli agenti IA non si limitano a chattare, ma hanno accesso a strumenti (es. possono eseguire query su un database o inviare email).
* **Il Delegato Confuso (Confused Deputy):** Se l'agente IA è dotato di privilegi elevati (Non-Human Identity - NHI), un attaccante potrebbe tramite una Prompt Injection convincere l'agente a usare i suoi privilegi per eseguire un'azione distruttiva (es. cancellare un record o autorizzare un bonifico). L'agente agisce come un "delegato" che è stato "confuso" dall'input malevolo.

---

## PARTE 3: Soluzioni Architetturali e di Sicurezza (Zero Trust per IA)
Per introdurre l'IA in un ambiente critico come la Banca d'Italia, l'infrastruttura tecnologica deve prevedere meccanismi di difesa in profondità.

### 1. AI Security Gateway e Guardrails
Il traffico verso l'LLM (le richieste degli utenti) non deve mai essere diretto. Si interpone un "Gateway" che esegue:
* **Input Sanitization e PII Scrubbing:** Filtra le richieste in ingresso per bloccare tentativi noti di Prompt Injection e maschera (anonimizza/pseudonimizza) eventuali Dati Personali (PII) prima che vengano inviati al modello, garantendo la conformità al GDPR.
* **Output Validation:** Verifica che la risposta generata dal modello non contenga allucinazioni evidenti, codice malevolo o fughe di dati finanziari riservati (Data Leakage Prevention).

### 2. Architettura RAG (Retrieval-Augmented Generation)
Per evitare che l'IA inventi risposte (Allucinazioni) o che la Banca debba cedere i propri dati per l'addestramento di modelli cloud pubblici, si utilizza l'approccio RAG.
* Il modello base (Foundation Model) non viene ri-addestrato. Invece, la query dell'utente viene prima confrontata vettorialmente con il database documentale interno e sicuro della Banca. I documenti rilevanti vengono estratti e passati al modello nel prompt come "contesto", costringendo l'IA a basare la risposta **esclusivamente sui documenti aziendali**. Questo garantisce precisione, aggiornamento e segregazione dei dati.

### 3. Isolamento e Identità per Agenti IA
* Gli agenti IA devono operare in **Sandbox** isolate, potendo accedere solo a un set minimo di API (Least Privilege).
* Ogni agente deve possedere un'identità verificabile (NHI) soggetta a log e monitoraggio tramite SIEM, per individuare comportamenti anomali in tempo reale.

---

> [!TIP]
> **Consiglio per il Tema d'Esame:**
> Se ti viene chiesto come introdurre l'Intelligenza Artificiale per l'analisi dei dati di vigilanza o per l'help-desk interno della Banca, struttura il progetto così:
> 1.  Dichiara che il sistema dovrà rispettare i requisiti di tracciabilità e trasparenza dell'**AI Act** (verificando se rientra nell'Alto Rischio).
> 2.  Proponi un'architettura **RAG** con LLM ospitato localmente o in un Private Cloud per garantire la **Data Sovereignty** ed evitare violazioni GDPR.
> 3.  Prevedi l'adozione di un **AI Security Gateway** per neutralizzare i rischi di Prompt Injection ed esfiltrazione dati.
> 4.  Assicura che l'output dell'IA sia considerato solo come supporto decisionale (Augmented Intelligence), prevedendo sempre il controllo umano (*Human-in-the-loop*).
