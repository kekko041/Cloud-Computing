# Simulazione — Ramo C: Architetture, Cloud, Migrazione & Qualità del Software
### Concorso AGID-01 · Materie 4, 5, 8 del bando (art. 7)

> **Formato.** Come da bando, la prova reale è composta da uno o più quesiti a risposta sintetica e uno o più casi gestionali, in 4 ore complessive su tutte le materie. Questa è una simulazione **parziale**, mirata al solo Ramo C — usala come allenamento a tempo, non come prova completa.
>
> **Timing consigliato:** 15' a quesito sintetico (30' totali) + 90' per il caso gestionale + 15-20' di autocorrezione con la griglia in fondo. ≈ 2h15 totali.
>
> **Metodo per il caso gestionale:** usa le "4 mosse" — (1) inquadramento normativo, (2) metodo progettuale, (3) soluzione tecnica, (4) rischio & budget — così come impostato nella [mappa mentale del concorso](Mappa_Mentale_AGID.html).
>
> **Fonti di riferimento:** [Sintesi_Architetture_Qualita_Migrazione.md](Sintesi_Architetture_Qualita_Migrazione.md), `AGID/Pubblicazioni_e_Linee_Guida_AGID.md` §4-5-8, `AGID/pdf/01`, `08-11`, `16-17`.

---

## Quesiti a risposta sintetica

### Quesito 1
> Il candidato illustri il significato di "Secure by Design" nel ciclo di sviluppo del software, descrivendo il ruolo del Threat Modeling e dei controlli SAST/DAST in una pipeline DevSecOps.

### Quesito 2
> Il candidato descriva il modello di qualità ISO/IEC 25010, indicando almeno quattro caratteristiche di qualità previste e come possano essere tradotte in criteri misurabili all'interno di un capitolato di gara ICT.

### Quesito 3
> Il candidato descriva i tre percorsi di migrazione al Cloud (Rehost, Replatform, Rearchitect/Refactor), indicando per ciascuno il livello di sforzo, il beneficio atteso e un esempio di caso d'uso in cui sarebbe la scelta più appropriata.

### Quesito 4
> Il candidato descriva cos'è il Polo Strategico Nazionale (PSN), per quali servizi ne è obbligatorio l'utilizzo e da chi è retto — indicando i soggetti coinvolti nell'indirizzo strategico, nella sicurezza, nella qualificazione tecnica e nella gestione operativa dell'infrastruttura.

### Quesito 5
> Il candidato, dopo aver illustrato il modello di qualità ISO/IEC 25010, discuta come le caratteristiche di **sicurezza** e **manutenibilità** possano essere tradotte in clausole contrattuali verificabili in un appalto pubblico di sviluppo software, motivando la scelta di eventuali penali e il relativo impatto su TCO e rischio di lock-in del fornitore.

---

## Caso gestionale

> Un'Agenzia centrale gestisce un sistema informativo legacy, monolitico, ospitato su server on-premise in un data center locale ormai obsoleto, che eroga un servizio classificato come **Critico** per la continuità dei procedimenti amministrativi. L'Agenzia deve pianificare la dismissione del data center locale entro 18 mesi, migrando il sistema verso un'infrastruttura conforme al principio Cloud First, e coglie l'occasione per migliorare la qualità e la sicurezza del software, storicamente carente di test automatizzati e controlli di sicurezza nel ciclo di sviluppo.
>
> Il candidato, assumendo il ruolo di responsabile architetture dell'Agenzia:
>
> **(a)** individui la destinazione infrastrutturale obbligata per un servizio Critico e motivi la scelta del percorso di migrazione (Rehost/Replatform/Rearchitect) più adeguato entro il vincolo temporale dato, valutando i trade-off tra sforzo e beneficio;
>
> **(b)** proponga le modifiche al ciclo di sviluppo per renderlo Secure by Design (threat modeling, SAST/DAST, hardening delle configurazioni), collegandole alle fasi della pipeline CI/CD;
>
> **(c)** indichi il modello di qualità e le metriche da adottare per misurare il miglioramento (ISO/IEC 25010, code coverage, densità difetti, tempo di remediation delle vulnerabilità) e come inserirle come requisiti in un eventuale capitolato di gara per il fornitore incaricato della migrazione;
>
> **(d)** analizzi i principali rischi dell'operazione (finestra di indisponibilità del servizio Critico, debito tecnico residuo, dipendenza dal fornitore/lock-in) e le relative misure di mitigazione, inclusi gli impatti di budget (TCO).
>
> Si motivino le scelte e si segnalino eventuali criticità residue.

---

## Griglia di autocorrezione

Usala per punteggiare (0/1/2) ciascuna voce dopo aver scritto la tua risposta.

**Quesito 1**
- [ ] Spiega Secure by Design come integrazione della sicurezza fin dalla fase di progettazione, non aggiunta a posteriori
- [ ] Descrive il Threat Modeling come identificazione dei rischi architetturali prima di scrivere codice
- [ ] Distingue SAST (analisi statica del codice) da DAST (test dinamico in esecuzione) e li colloca in una pipeline CI/CD continua (DevSecOps)

**Quesito 2**
- [ ] Cita correttamente almeno 4 caratteristiche ISO/IEC 25010 (funzionalità, affidabilità, usabilità, sicurezza, manutenibilità, portabilità)
- [ ] Traduce almeno una caratteristica in una metrica misurabile (es. affidabilità → MTBF/MTTR, sicurezza → tempo di remediation)
- [ ] Collega il modello di qualità ai criteri di valutazione in un capitolato di gara ICT

**Quesito 3**
- [ ] Descrive correttamente i tre percorsi (Rehost = lift&shift IaaS; Replatform = modifiche minime, es. DBaaS; Rearchitect/Refactor = cloud-native, microservizi/container/serverless)
- [ ] Indica correttamente la relazione sforzo/beneficio crescente da Rehost a Rearchitect
- [ ] Propone un caso d'uso plausibile e coerente per almeno due dei tre percorsi

**Quesito 4**
- [ ] Definisce il PSN come infrastruttura cloud sovrana obbligatoria per i servizi/dati classificati Critici e Strategici (non un ente pubblico, ma un'infrastruttura in concessione)
- [ ] Indica correttamente l'indirizzo strategico (Presidenza del Consiglio – Dip. Trasformazione Digitale) e il ruolo dell'ACN nei requisiti di sicurezza/classificazione, distinto dal ruolo di AGID nella qualificazione dei cloud provider
- [ ] Cita Difesa Servizi S.p.A. come stazione appaltante della concessione (per la rilevanza securitaria) e PSN S.p.A. (consorzio TIM-CDP Equity-Sogei-Leonardo) come concessionario gestore per 15 anni
- [ ] Non confonde i piani: indirizzo politico ≠ vigilanza di sicurezza ≠ qualificazione tecnica ≠ gestione operativa privata in concessione

**Quesito 5**
- [ ] Definisce correttamente sicurezza (riservatezza, integrità, non ripudio, autenticità) e manutenibilità (modularità, testabilità, analizzabilità) secondo ISO/IEC 25010
- [ ] Propone almeno 2 metriche verificabili per ciascuna caratteristica (es. sicurezza → tempo di remediation per severità; manutenibilità → code coverage e densità difetti)
- [ ] Collega le metriche a clausole contrattuali con penali graduate per gravità/ritardo
- [ ] Discute il trade-off tra soglie troppo stringenti (aumento costi/tempi del fornitore) e soglie troppo blande (rischio qualità non presidiato), con impatto su TCO e lock-in

**Caso gestionale**

| Punto | Cosa deve comparire nella risposta | ✓ |
|---|---|---|
| (a) Infrastruttura e percorso | Servizio Critico → obbligo di destinazione al Polo Strategico Nazionale (PSN); scelta motivata del percorso (es. Replatform come compromesso tra vincolo temporale di 18 mesi e miglioramento rispetto al puro Rehost) | ☐ |
| (b) Secure by Design | Threat modeling in fase di analisi, SAST/DAST integrati in pipeline CI/CD, hardening delle configurazioni (All. C) | ☐ |
| (c) Qualità e capitolato | ISO/IEC 25010 come framework, metriche operative concrete (code coverage, densità difetti, tempo di remediation), loro traduzione in requisiti contrattuali/KPI di gara | ☐ |
| (d) Rischi e budget | Finestra di indisponibilità del servizio Critico (piano di rollback/cutover), debito tecnico residuo, lock-in del fornitore cloud, TCO del percorso di migrazione scelto | ☐ |
| Metodo | La risposta segue le 4 mosse (norma → metodo → soluzione tecnica → rischio/budget) invece di elencare i fatti senza struttura | ☐ |

---

> **Come proseguire.** Scrivi la tua risposta al caso gestionale (anche solo per punti) e incollala in chat: te la correggo voce per voce sulla griglia sopra, segnalando cosa manca e cosa è già solido.
