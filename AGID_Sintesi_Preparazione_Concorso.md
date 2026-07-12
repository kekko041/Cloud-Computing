# Sintesi Preparazione Concorso (Profilo AGID-01)
*Basata sulle Linee Guida, Piano Triennale e Documentazione AGID/ACN*

Questa sintesi organizza organicamente il materiale ufficiale scaricato per facilitare il ripasso strutturato delle materie d'esame. È concepita con un taglio da "Systems Engineer e ICT Consultant", privilegiando architetture, sicurezza e aderenza normativa.

---

## 1. Interoperabilità e Piattaforme (ModI & PDND)
L'obiettivo della digitalizzazione è superare la logica dei "silos" informatici, permettendo ai sistemi della PA di comunicare tra loro.
*   **Modello di Interoperabilità (ModI):** Definisce le regole tecniche per lo scambio dati tramite **API** (REST e SOAP).
    *   *Sicurezza:* Impone l'autenticazione tramite certificati X.509, integrità del payload, e pattern di sicurezza come **OAuth 2.0** (per l'autorizzazione) e **mTLS** (Mutual TLS per l'autenticazione server-to-server).
*   **PDND (Piattaforma Digitale Nazionale Dati):** È l'infrastruttura tecnologica che realizza il ModI. Permette alle PA di esporre (E-Service) e fruire di dati tramite un Catalogo API centrale.
    *   *Principio Chiave:* **Once Only**. Il cittadino non deve fornire dati che un'altra PA possiede già; le PA se li scambiano tramite PDND.

## 2. Cloud, Architetture e Migrazione
La PA adotta il principio **Cloud First**: le nuove iniziative e gli aggiornamenti infrastrutturali devono prediligere soluzioni Cloud (SaaS > PaaS > IaaS) per ridurre i costi, aumentare la scalabilità e garantire resilienza.
*   **Strategia Cloud Italia:** Classifica i dati della PA in tre livelli: *Ordinari*, *Critici* e *Strategici*. I dati Critici e Strategici devono risiedere su infrastrutture ad altissima affidabilità (come il **Polo Strategico Nazionale - PSN**).
*   **Percorsi di Migrazione:** Il Manuale AGID prevede tre approcci principali:
    1.  *Rehost (Lift & Shift):* Spostamento delle VM senza modifiche (IaaS).
    2.  *Replatform:* Uso di piattaforme gestite (es. DBaaS) con minime modifiche al codice.
    3.  *Rearchitect / Refactor:* Riprogettazione cloud-native (microservizi, container, serverless), per sfruttare appieno i benefici del cloud (massimo effort, massima resa).
*   **Qualificazione ACN/AGID:** I Cloud Service Provider (CSP) devono essere accreditati tramite un processo rigido di valutazione della sicurezza e inseriti in un marketplace dedicato.

## 3. Sviluppo Software: Acquisizione, Riuso e Sicurezza
Le metriche del software per la PA non si limitano alle prestazioni, ma includono sicurezza nativa e riusabilità.
*   **Acquisizione (Artt. 68-69 CAD):** Prima di acquistare un software proprietario, una PA deve eseguire una valutazione comparativa. L'ordine di preferenza è:
    1.  Software Open Source.
    2.  Software in riuso (già sviluppato da altra PA).
    3.  Sviluppo ex novo (che dovrà poi essere messo in riuso con licenza aperta).
    4.  Software proprietario (solo se strettamente necessario e motivato).
*   **Sviluppo Sicuro (Secure by Design):** Il ciclo di vita del software (SDLC) deve integrare la sicurezza dalla fase di design. 
    *   *Modellazione delle Minacce (Threat Modeling):* Identificare i rischi architetturali prima di scrivere il codice.
    *   *Controlli:* SAST (Static Application Security Testing) e DAST (Dynamic) continui (DevSecOps).
    *   *Linee guida OWASP:* Prevenzione di Injection, Broken Authentication e vulnerabilità note.

## 4. Dati: Documento Informatico, Open Data e IA
La gestione del patrimonio informativo (modellazione e metadatazione) è al centro della *data-driven administration*.
*   **Documento Informatico:** Equiparato alla carta, se formato e conservato secondo le regole tecniche.
    *   *Firme (eIDAS):* FES (semplice), FEA (avanzata) e FEQ (qualificata/digitale, garantisce non ripudio e integrità).
    *   *Metadatazione:* Ogni documento informatico deve avere un set minimo di metadati obbligatori (es. identificativo, data, oggetto, autore) per garantirne la rintracciabilità e fascicolazione elettronica.
*   **Open Data:** I dati pubblici (non soggetti a privacy) devono essere pubblicati in formati aperti, machine-readable (es. CSV, JSON) e descritti da ontologie (come *OntoPiA*) per garantirne la semantica condivisa.
*   **Intelligenza Artificiale:** L'impiego del Machine Learning nella PA deve rispettare l'**AI Act** europeo (trasparenza algoritmica, assenza di bias, supervisione umana per decisioni critiche).

## 5. Programmazione, Budget e Governo IT
L'azione della PA deve essere programmata, misurabile e finanziariamente sostenibile.
*   **Piano Triennale per l'Informatica:** È lo strumento di governance strategica (attualmente 2024-2026). Definisce i target di trasformazione digitale (es. percentuale di servizi migrati in cloud, adozione SPID).
*   **Formazione del Budget:** La spesa ICT non è più vista come "centro di costo", ma come "investimento". Si basa su logiche di TCO (Total Cost of Ownership), tenendo conto anche dei costi di lock-in, formazione ed energy saving (Green IT).
*   **Gestione Progettuale:** Si raccomanda l'uso di framework strutturati (PRINCE2, PMP, o framework Agile) con KPI chiari e misurabili, essenziali per la rendicontazione dei fondi PNRR.

## 6. Appalti e Trasparenza 
L'infrastruttura amministrativa che permette la realizzazione tecnica dei progetti.
*   **Codice degli Appalti (D.Lgs. 36/2023):** Tutto il ciclo di gara (ICT e non) è interamente digitale (e-Procurement, Fascicolo Virtuale Operatore Economico). Acquisti IT gestiti tramite Consip/MePA. Liberalizzato (ma attenzionato lato cyber) il subappalto.
*   **Performance e Trasparenza:** 
    *   *Accessibilità:* I servizi digitali (Web/App) devono seguire le linee guida **WCAG 2.1** (Legge Stanca), garantendo usabilità a persone con disabilità visive, motorie o cognitive.
    *   *Design:* Coerenza visiva e centralità dell'utente (UX/UI standardizzate da *Designers Italia*).
    *   *Amministrazione Trasparente:* Obbligo di pubblicazione sui portali istituzionali dei dati relativi a bandi, appalti, bilanci e performance dirigenziali (D.Lgs. 33/2013).

---
> [!TIP] 
> **Come usare questo riassunto per la prova scritta (Profilo A/C)**
> Quando affronti un **caso pratico gestionale** (es. "Progettare la migrazione di un database on-premise"), usa una struttura logica che tocchi questi punti:
> 1. **Architettura:** Migrazione Replatform sul Cloud PSN (Punto 2).
> 2. **Sicurezza:** Cifratura at-rest e in-transit, Threat modeling (Punto 3).
> 3. **Acquisizione:** Uso di MePA/Consip (Punto 6) e preferenza Open Source (Punto 3).
> 4. **Integrazione:** Esposizione API REST tramite PDND (Punto 1).
