# Domande aperte per l'orale DTD1 — con traccia di risposta

> Ogni traccia è una **scaletta**, non un testo da imparare a memoria: espandila con lo schema in 5 punti (`01_Metodo_Orale_DTD1.md`). Approfondimenti nei file `studio/` e `MIT/orale/domande_aperte_per_materia.md` (materie tecniche).

## ⭐ Le 10 domande "probabilissime"
1. Che cos'è il Dipartimento per la trasformazione digitale e come si colloca nella PCM? → §9.1
2. Differenza tra progetto, programma e portfolio; come si gestiscono i benefici? → §1.1
3. Come governeresti un programma PNRR di migrazione al cloud di centinaia di Comuni? → §1.4 + §8.3
4. Le misure di M1C1: quali sono e come funziona il meccanismo lump sum? → §8.2
5. Principi del D.Lgs. 36/2023 e digitalizzazione del ciclo di vita dei contratti → §6.1-6.3
6. Che cos'è la PDND e come funziona l'interoperabilità tra PA? → §2.4
7. Privacy by design e DPIA in un nuovo servizio digitale → §7.2
8. NIS2 e il ruolo di ACN; misure di sicurezza per una PA → §7.4
9. IA nella PA: AI Act, L. 132/2025, rischi e opportunità → §5.3
10. Architettura di un servizio cloud ad alta disponibilità → §2.2

---
## 1. Project e Program management (8 quesiti su 40 allo scritto ⇒ priorità)
**1.1 Progetto vs programma vs portfolio.**
- Progetto = sforzo temporaneo con **output** definiti; programma = progetti correlati gestiti in modo coordinato per ottenere **benefici e outcome**; portfolio = **selezione e prioritizzazione** di progetti e programmi rispetto alla strategia.
- **Catena del valore (MSP)**: output → **capability** → **outcome** → **benefici** (misurabili) → obiettivi strategici. Possibili *dis-benefici*.
- Esempio: il PNRR M1C1 è un **portfolio** di misure; "PA digitale 2026" è un **programma**; la migrazione di un singolo Comune è un **progetto**.

**1.2 Governance di un programma.**
- Ruoli (MSP):
  - **Sponsoring Group** (vertice, impegno strategico);
  - **SRO – Senior Responsible Owner** (risponde del programma e dei benefici);
  - **Programme Manager** (coordina i progetti, gestisce rischi e interdipendenze);
  - **Business Change Manager** (realizza i benefici nell'organizzazione utente);
  - **PMO di programma**.
- Documenti:
  - **Program Charter** / mandato;
  - **Vision statement** e **Blueprint** (*target operating model*);
  - **Benefits Map**, **Benefits Realization Plan**, profili dei benefici con KPI, owner e baseline;
  - roadmap a **tranche**, registro dei rischi e delle issue, **Communications Management Plan**, piano degli stakeholder.
- **Gestione delle modifiche**: soglie di tolleranza. Il CCB di progetto decide le modifiche locali; **escala** al **CCB di programma** se le modifiche toccano interdipendenze, budget di programma o benefici (Q37 dello scritto).

**1.3 Gestire un cambiamento normativo che rende obsoleti dei target.**
- **Analisi d'impatto** sul **Benefits Realization Plan** → proposta allo **Sponsoring Group** di **riallineare formalmente** Charter e baseline → rimodulare, chiudere o avviare progetti (Q20).
- Per il PNRR: la modifica dei target avviene solo con la **revisione del Piano** negoziata con la Commissione UE.

**1.4 Bassa adozione di una piattaforma rilasciata (OCM).**
- Il problema raramente è tecnico. Analisi delle barriere con **ADKAR** (*Awareness, Desire, Knowledge, Ability, Reinforcement*) o **Kotter** (8 passi).
- Leve: **sponsorship visibile**, rete di **change agent** negli enti, formazione mirata, help desk, comunicazione dei benefici, misura dell'adozione (KPI d'uso) e rinforzo (Q19).
- Per il DTD: rete dei **facilitatori digitali**, community dei RTD, kit di Designers Italia e Developers Italia.

**1.5 Risorse e tempi.**
- **Resource leveling** (rispetta il vincolo della risorsa, **può allungare** il percorso critico → ri-baseline) vs **resource smoothing** (usa solo il float). Per una risorsa scarsa condivisa tra progetti (es. architetto cloud), la priorità si decide **a livello di programma** (Q43).
- **Riserve**: contingency (rischi noti, nella baseline, gestita dal PM) vs management reserve (ignoti, fuori dalla baseline, sbloccata dallo sponsor) (Q22).
- **EVM**: CPI, SPI, EAC (`studio/04` §1).

**1.6 Economie di gara in un programma finanziato.**
- Verificare l'**ammissibilità della spesa** e i **vincoli di destinazione** del fondo → proposta di riallocazione **approvata** dallo Sponsoring Group e dall'**autorità di gestione/titolare della misura**.
- Nel PNRR: tracciabilità su **ReGiS**, divieto di doppio finanziamento, coerenza con milestone e target (Q23).

**1.7 Procurement di programma.**
- Allineare i contratti dei diversi fornitori alle **milestone di programma**; clausole standard di **integrazione e cooperazione tra fornitori**, SLA, passaggio di consegne ed **exit strategy**; accordi quadro Consip (Q34).

**1.8 Agile nella PA.** Scrum e Kanban; come conciliarli con contratti e collaudi: contratti con **lotti/sprint a misura**, Definition of Done concordata, **MVP**, verifica di conformità incrementale. Approccio **ibrido**: governance predittiva a livello di programma, delivery agile nei progetti.

**1.9 Comunicazione di crisi** (guasto con risonanza mediatica): attivare la **procedura di crisi** del Communications Plan, **un unico portavoce**, informare subito lo Sponsoring Group con analisi d'impatto e piano di ripristino, comunicazioni regolari e verificate (Q29).

---
## 2. Sistemi informativi, architetture ICT, reti
**2.1 Rete di una sede PA.** Topologia **gerarchica** (access / distribution / core) con ridondanza (Q31); **VLAN** per segmenti (ospiti, uffici, OT) + **firewall** tra le sottoreti con regole minime (Q27); Wi-Fi WPA3-Enterprise con 802.1X; **NAC**; monitoraggio con **SNMPv3** (autenticazione e cifratura) o telemetria (Q1); collegamento tra sedi con **VPN IPsec site-to-site** (Q17) o SD-WAN; **IPv6** con SLAAC/DHCPv6 (Q18).

**2.2 Servizio cloud ad alta disponibilità.**
- Istanze **stateless** su **più availability zone** dietro un **load balancer** con *health check*; database replicato (sincrono nella regione, asincrono per il **DR** in un'altra regione); autoscaling; backup immutabili (Q54).
- **RTO/RPO** definiti con il business; test di failover; osservabilità (log, metriche, tracing; **SLI/SLO**).
- Nella PA: **cloud qualificato ACN** e classificazione dei dati **ordinari / critici / strategici** → PSN per i dati critici e strategici.

**2.3 Modelli architetturali.** Monolite modulare vs microservizi (vantaggi: scalabilità e deploy indipendenti; costi: complessità operativa, consistenza eventuale, osservabilità); API gateway; architettura a eventi (code, *pub/sub*); **12-factor app**; container e Kubernetes.

**2.4 Interoperabilità (PDND e ModI).**
- Base giuridica: **art. 50-ter CAD**; **Linee guida AgID sull'interoperabilità tecnica** (*ModI*: REST/OpenAPI, profili di sicurezza, firma e integrità dei messaggi).
- **PDND** (gestita da PagoPA S.p.A.): **catalogo di e-service**, accordi di fruizione, **voucher** (token OAuth2/JWT) per autorizzare le chiamate, principio **once only**.
- Esempio: ANPR esposta via PDND ai Comuni e agli enti.
- Rischi: qualità e responsabilità del dato. Servono **owner del dato** e regole di aggiornamento, oltre al collaudo tecnico (Q16).

**2.5 Migrazione al cloud.** Le **6R** (rehost, replatform, refactor, repurchase/SaaS, retire, retain); assessment; Strategia Cloud Italia; manuale di abilitazione al cloud e **Cloud Enablement Kit** (`AGID/pdf/16-17`); rischio di **lock-in** → standard aperti, portabilità, exit plan.

**2.6 Sistema informativo vs sistema informatico; ERP, DMS e protocollo informatico; SPC.**

---
## 3. Data management
**3.1 Dal transazionale all'analitico.** OLTP separato dall'OLAP: **DWH** alimentato con ETL/ELT, dati storicizzati e integrati (Q55); **schema a stella** vs a fiocco di neve (Q59); **data mart dipendenti** (Q42); data lake e lakehouse.

**3.2 ETL vs ELT.** Nell'ELT le trasformazioni avvengono **nella destinazione** → servono governance, **lineage**, qualità all'ingresso e versionamento delle regole (Q41).

**3.3 Data governance in una PA.**
- Ruoli: owner, steward, custodian. Strumenti: catalogo e **metadati** (DCAT-AP_IT), qualità (**ISO/IEC 25012**: accuratezza, completezza, coerenza, attualità…), **master data** (anagrafiche uniche, Q30 dello scritto: una **fonte di riferimento** + controlli di allineamento).
- **Validazione** prima della pubblicazione (Q25). **Basi di dati di interesse nazionale** (art. 60 CAD).

**3.4 Open data.** Open by default (art. 52 CAD); D.Lgs. 36/2006 (Direttiva UE 2019/1024); **dati di elevato valore** (Reg. UE 2023/138: geospaziali, osservazione della Terra e ambiente, meteo, statistica, imprese, mobilità) da pubblicare **gratuitamente tramite API**; portale **dati.gov.it**; licenza **CC-BY 4.0**; modello a 5 stelle.

**3.5 Transazioni.** ACID; anomalie e **livelli di isolamento** (Serializable impedisce i fantasmi, Q12); lock vs MVCC; indici ed EXPLAIN; normalizzazione (3NF).

**3.6 NoSQL e big data.** Teorema CAP; documentali, chiave-valore, colonnari, a grafo; Spark e streaming.

---
## 4. Programmazione, sviluppo software, web
**4.1 Ciclo di sviluppo sicuro (LG AgID sviluppo sicuro, `AGID/pdf/08-11`).**
- *Security by design*: **threat modeling** (STRIDE); OWASP ASVS e Top 10; **SAST/DAST/SCA**; **SBOM** = inventario di componenti e dipendenze (Q56; richiesto anche dal **Cyber Resilience Act**); gestione dei segreti; pipeline **CI/CD** con *quality gate*.

**4.2 Qualità del codice.** **Refactoring** = migliorare la struttura senza cambiare il comportamento (Q38), protetto dai test; debito tecnico; SOLID; code review; test pyramid; **Git** (branching, **rebase** vs merge, Q60).

**4.3 API REST.** Risorse, verbi, idempotenza, status code, versionamento, **OpenAPI**, paginazione, rate limiting, autenticazione **OAuth2/OIDC** e JWT (verifica di firma, `exp`, `iss`, `aud`).

**4.4 Sicurezza web.** Cookie **HttpOnly** (non leggibili da JS, Q49) / Secure / SameSite; CSP; CORS; protezione da XSS, CSRF, SQL injection.

**4.5 Riuso e open source nella PA.** Artt. 68-69 CAD; LG acquisizione e riuso del software; **Developers Italia**, `publiccode.yml`; **Designers Italia** (UI kit, modelli dei siti dei Comuni); **accessibilità** (L. 4/2004, WCAG 2.1 AA, dichiarazione di accessibilità entro il 23 settembre).

---
## 5. Intelligenza artificiale
**5.1 Concetti di base.**
- **Test di Turing** (gioco dell'imitazione, Q32); IA simbolica vs apprendimento automatico; supervisionato, non supervisionato, per rinforzo.
- Reti neurali: la **discesa del gradiente minimizza la loss** (Q40). Transformer e LLM.
- **NLP**: NER, traduzione automatica, sentiment, sintesi (Q44); computer vision (riconoscimento facciale, segmentazione) è un'altra area.

**5.2 Rischi dell'IA generativa.** **Allucinazioni** (Q52) → RAG su fonti istituzionali, citazioni, *human in the loop*; prompt injection; bias; data leakage e privacy; diritto d'autore; trasparenza.

**5.3 Quadro normativo.**
- **AI Act (Reg. UE 2024/1689)**: approccio per livelli di rischio; obblighi di provider e deployer; **FRIA** (valutazione d'impatto sui diritti fondamentali) per gli enti pubblici che usano sistemi ad alto rischio; alfabetizzazione IA.
- **L. 132/2025**: autorità **AgID** (notifica e promozione) e **ACN** (vigilanza); nella PA l'IA **supporta** la decisione, la cui responsabilità resta al funzionario; principi di conoscibilità e tracciabilità.
- **Linee guida AgID** per l'adozione dell'IA nella PA; Strategia italiana IA 2024-2026; Piano Triennale.

**5.4 Caso: un chatbot per i cittadini.**
- Requisiti e metriche; base di conoscenza istituzionale con **RAG**; trasparenza ("stai parlando con un'IA", art. 50 AI Act); privacy (DPIA, minimizzazione, non addestrare sui dati degli utenti senza base giuridica); escalation a un operatore umano; monitoraggio della qualità; acquisizione tramite appalto con clausole su dati, sicurezza e portabilità.

---
## 6. Appalti pubblici (D.Lgs. 36/2023) — 2 errori su 3 allo scritto ⇒ priorità
**6.1 Principi.** **Risultato** (art. 1), **fiducia** (art. 2), **accesso al mercato** (art. 3) come criterio interpretativo (art. 4); buona fede; auto-organizzazione (in house); equilibrio contrattuale; tassatività delle cause di esclusione.

**6.2 RUP.** Responsabile **unico del progetto** (art. 15, **All. I.2**): nominato nella fase di avvio, fra i dipendenti con competenze adeguate. **c.4**: si possono nominare un responsabile di procedimento per **programmazione, progettazione ed esecuzione** e uno per l'**affidamento** (Q33). Il RUP **resta responsabile** del coordinamento complessivo.

**6.3 Digitalizzazione (artt. 19-36).**
- **Principi digitali dell'art. 19**: tra questi l'**unicità dell'invio** — ogni dato è fornito **una sola volta a un solo sistema informativo**, non può essere richiesto da altri sistemi ed è reso disponibile dal sistema ricevente (Q48).
- Ecosistema nazionale di e-procurement; **BDNCP** (ANAC); **FVOE**; **piattaforme certificate** (regole AgID); interoperabilità con la PDND; accesso agli atti digitale.

**6.4 Sotto soglia.** Affidamento diretto (< 140k servizi e forniture, < 150k lavori), procedura negoziata (5/10 operatori), rotazione (art. 49), MePA.

**6.5 Esecuzione.**
- **Verifica di conformità** per servizi e forniture (**art. 116**; collaudo per i lavori): certifica il rispetto delle caratteristiche tecniche, economiche e qualitative, degli obiettivi e dei tempi; per le prestazioni periodiche si svolge **durante l'esecuzione**; modalità e tempi sono definiti nel capitolato (Q58).
- **DEC**, penali, modifiche contrattuali (art. 120), subappalto (art. 119), revisione prezzi (art. 60).

**6.6 Caso: acquisire una piattaforma SaaS per un ente.**
- Analisi del fabbisogno e valutazione comparativa (art. 68 CAD) → verifica di Convenzioni o Accordi quadro **Consip** (obbligo per l'ICT) → **catalogo dei servizi cloud qualificati ACN** → criterio **OEPV** → clausole su SLA, sicurezza, localizzazione e portabilità dei dati, exit strategy → DEC e verifica di conformità.

---
## 7. Privacy e sicurezza
**7.1 GDPR, principi e basi giuridiche.**
- **Art. 5** (7 principi), **art. 6** (per la PA: obbligo legale / interesse pubblico).
- **Art. 9**: divieto generale per le categorie particolari, **con 10 eccezioni**, tra cui il consenso esplicito, l'**interesse vitale** dell'incapace e i motivi di **interesse pubblico rilevante** (Q2).
- **Art. 2-sexies del Codice privacy**: nella PA il trattamento per interesse pubblico rilevante richiede una **base normativa**.

**7.2 Privacy by design e DPIA.**
- **Art. 25**; **art. 35**: DPIA quando c'è un rischio elevato (criteri WP248: profilazione, dati sensibili su larga scala, monitoraggio sistematico, nuove tecnologie come l'IA); consultazione preventiva del Garante (art. 36) se il rischio residuo è elevato; coinvolgimento del **DPO** (obbligatorio per le PA).
- **Minimizzazione** e **limitazione della conservazione** (Q5); dati reali **non** in ambiente di test (Q11).

**7.3 Diritti e informativa.**
- Artt. 13-14: l'informativa per dati **non raccolti presso l'interessato** (art. 14) include categorie di dati, fonte e destinatari; **non** include le "condanne antiriciclaggio" (Q51).
- Diritti degli artt. 15-22; data breach (artt. 33-34: Garante entro **72 h**).

**7.4 Cybersicurezza nella PA.**
- **ACN** (D.L. 82/2021); **NIS2** (D.Lgs. 138/2024: soggetti essenziali e importanti, misure di base, notifiche 24 h / 72 h / 1 mese, **responsabilità degli organi di vertice**, piattaforma ACN); **L. 90/2024** (PA: struttura e **referente per la cybersicurezza**, notifica degli incidenti); PSNC; Strategia nazionale di cybersicurezza 2022-2026.
- Misure: **MFA**, Zero Trust, segmentazione, patching, EDR, SIEM/SOC, backup **3-2-1** immutabili con **test di ripristino** e credenziali separate (Q14); formazione contro il phishing.

**7.5 Caso: un dipendente segnala un ransomware.** Isolare le macchine dalla rete; attivare il piano di risposta agli incidenti (CSIRT interno → **CSIRT Italia**); preservare le evidenze; valutare il **data breach** (DPO → Garante entro 72 h); ripristinare da backup puliti; analisi della causa radice; comunicazione; *lessons learned*. **Non pagare il riscatto.**

---
## 8. PNRR — 0/2 allo scritto ⇒ priorità
**8.1 Architettura del PNRR.** RRF (Reg. UE 2021/241), 7 missioni, riforme + investimenti, milestone e target, rate semestrali, DNSH, tagging verde e digitale, Mezzogiorno; governance (D.L. 77/2021, Struttura di missione presso la PCM, Ispettorato generale per il PNRR del MEF, ReGiS); scadenza **2026**.

**8.2 M1C1 e il DTD.**
- Investimenti 1.1-1.7 (si veda `studio/02`).
- **Riforme**:
  - **1.1 "Processo di acquisto TIC"**: percorso **fast track** per gli acquisti ICT PNRR (Q47);
  - 1.2 supporto alla trasformazione delle PA;
  - 1.3 cloud first e interoperabilità.
- **Semplificazione**: digitalizzazione delle procedure **SUAP e SUE**, con dati accessibili su **"Impresa in un giorno"** (Q24).
- Avvisi **PA digitale 2026** con **lump sum** + **asseverazione** dei risultati.

**8.3 Caso: centinaia di Comuni devono completare la migrazione entro la scadenza.**
- Cruscotto di monitoraggio per ente e per fase → **segmentazione** dei ritardi (competenze, fornitore, dati) → supporto mirato (*Transformation Office* territoriali, webinar, FAQ, team di affiancamento: **sono proprio i 58 posti DTD1 da allocare sul territorio**) → escalation dei casi critici → gestione dei rischi sul target nazionale (scenario B: rimodulazione) → asseverazione ed erogazione.

**8.4 Dopo il PNRR.**
- Il **D.L. 19/2026** garantisce la continuità dei programmi e il rafforzamento del DTD;
- obiettivi del **Decennio digitale 2030** (Decisione UE 2022/2481) e Strategia Italia Digitale 2026;
- sostenibilità dei servizi (costi di esercizio, competenze interne, manutenzione evolutiva).

---
## 9. Ordinamento della PCM — 0/2 allo scritto ⇒ priorità
**9.1 Che cos'è il DTD.**
- **Art. 24-ter del DPCM 1/10/2012** (inserito dal DPCM 19/06/2019): struttura di supporto al PdC per la **strategia unitaria** di trasformazione digitale, che attua le direttive del Presidente e **coordina ed esegue i programmi**.
- Vigila su **PagoPA S.p.A.** (art. 8 D.L. 135/2018); rappresenta il Governo nelle sedi internazionali sull'agenda digitale.
- Con il DPCM 13/05/2026: fino a **3 Uffici e 8 Servizi**.
- Opera per l'**autorità politica delegata** all'innovazione tecnologica e alla transizione digitale.
- **Differenza con AgID**: AgID è un'**agenzia** con personalità giuridica che **attua** (linee guida, Piano Triennale, regole tecniche); il DTD è una **struttura interna** della PCM che **indirizza** e **coordina** (oltre a essere titolare delle misure PNRR). Con l'**ACN**, il DTD condivide la Strategia Cloud.

**9.2 Fonti dell'ordinamento PCM.** Artt. 92-96 Cost.; **L. 400/1988**; **D.Lgs. 303/1999** (autonomia organizzativa, contabile e di bilancio: il PdC individua con propri decreti le aree funzionali e il numero di uffici e servizi; l'organizzazione interna spetta al Segretario generale o ai Ministri e Sottosegretari delegati); **DPCM 1/10/2012** (strutture generali); **DPCM 10/04/2024** (autonomia finanziaria e contabile).

**9.3 Strutture e funzioni** (`orale/04`): affari regionali (art. 12, Conferenza Stato-Regioni), Casa Italia (art. 12-bis), funzione pubblica (art. 14), coordinamento amministrativo (art. 29, Commissione per l'accesso), Ufficio controllo interno (art. 31), personale (art. 34), servizi strumentali (art. 34-bis).

**9.4 Organi.** PdC (art. 95 Cost.; art. 5 L. 400: indirizzo, coordinamento, **sospensione** degli atti dei Ministri); CdM (art. 2); Ministri senza portafoglio (art. 9); Sottosegretario alla Presidenza (segretario del CdM); Segretario generale (vertice amministrativo).

**9.5 Atti normativi del Governo.** Decreti-legge (art. 77 Cost., 60 gg); decreti legislativi (art. 76 Cost.); regolamenti (art. 17 L. 400: governativi con parere del Consiglio di Stato, di delegificazione, ministeriali); DPCM (atti amministrativi o regolamentari del Presidente).

---
## 10. Domande trasversali e motivazionali
- Perché il DTD? Che cosa porti dalla tua esperienza? Quali sono i tuoi punti deboli? (Indica un limite reale e come ci stai lavorando.)
- Come spiegheresti a un sindaco di un piccolo Comune perché migrare al cloud? (Linguaggio semplice: sicurezza, costi, continuità, fondi disponibili.)
- Un fornitore non rispetta gli SLA: che cosa fai? (Evidenze → DEC/RUP → contestazione formale → penali → piano di rientro.)
- Come ti aggiorni professionalmente? (Fonti istituzionali: AgID, ACN, ENISA, community di Developers Italia, certificazioni.)
- Etica pubblica: art. 54 Cost. (disciplina e onore); **codice di comportamento** dei dipendenti pubblici (DPR 62/2013, aggiornato dal DPR 81/2023, con norme sull'uso dei **social** e delle tecnologie); conflitto d'interessi; whistleblowing (D.Lgs. 24/2023).
