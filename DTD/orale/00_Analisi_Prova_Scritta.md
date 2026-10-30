# Analisi della prova scritta DTD1 — 29/10/2026

> Fonte: `DTD/scritto/COMPITO_PNNSNT80E24L736W-2.pdf`. Nel PDF la risposta corretta è indicata in verde e la risposta errata data in rosso; le ho estratte leggendo il colore del testo.

## 1. Esito
| Voce | Valore |
|---|---|
| **Punteggio** | **43,5 / 60** — SUPERATA (minimo 42) |
| Corrette / errate / non date | 46 / 5 / 9 |
| Formato reale | **4 opzioni** (non 3 come al MIT) → tirare a caso ha valore atteso **−0,125**: hai fatto bene a lasciare in bianco i dubbi |

### Composizione del punteggio
| Blocco | Risultato | Punti |
|---|---|---|
| Situazionali (12) | **12/12 "più efficace"** ✅ | 12 |
| Inglese (8) | 7 corrette, 1 non data (Q4) | 7 |
| Materie (40) | 27 corrette, 5 errate, 8 non date | 27 − 2,5 = 24,5 |
| **Totale** | | **43,5** |

## 2. Risultato per materia (40 quesiti di materia)
| Materia | Quesiti | ✅ | ❌ | ∅ | Note |
|---|---|---|---|---|---|
| 1. Project & **Program** management | **8** (19, 20, 22, 23, 29, 34, 37, 43) | 5 | 0 | 3 | **Materia più pesante**: tutte domande di *program* management (benefici, CCB, resource leveling, riserve) |
| 2. Sistemi, architetture, reti | 6 (1, 17, 18, 27, 31, 54) | **6** | 0 | 0 | punto di forza |
| 3. Data management | 7 (12, 21, 25, 41, 42, 55, 59) | 5 | 1 | 1 | DWH e livelli di isolamento |
| 4. Programmazione e web | 4 (38, 49, 56, 60) | 3 | 1 | 0 | refactoring ⚠️ |
| 5. Intelligenza artificiale | 4 (32, 40, 44, 52) | **4** | 0 | 0 | punto di forza |
| 6. Appalti (D.Lgs. 36/2023) | 3 (33, 48, 58) | 1 | **2** | 0 | domande **per articolo** |
| 7. Privacy e sicurezza | 4 (2, 5, 14, 51) | 3 | 1 | 0 | art. 9 GDPR |
| 8. PNRR | 2 (24, 47) | 0 | 0 | **2** | misure di dettaglio M1C1 |
| 9. Ordinamento PCM | 2 (8, 57) | 0 | 0 | **2** | **DPCM 1/10/2012** articolo per articolo |

**Diagnosi.**
- Materie **tecniche** (1-5): **23/29** (79%).
- Materie **normative** (6-9): **4/11** (36%) e **2 errori su 5**. All'orale queste materie avranno un peso proporzionalmente maggiore: un funzionario PCM deve conoscerle. **Sono la priorità del ripasso.**

## 3. Le domande sbagliate o non date — correzione
| Q | Tema | Tua risposta | Risposta corretta e perché |
|---|---|---|---|
| **2** ❌ | GDPR, categorie particolari (art. 9) | "è sempre vietato" | **Ammesso se necessario per tutelare un interesse vitale** dell'interessato incapace di dare il consenso. L'art. 9 par. 1 pone un **divieto generale**, ma il par. 2 prevede **10 eccezioni** (consenso esplicito, diritto del lavoro, **interesse vitale**, ONLUS, dati resi pubblici dall'interessato, diritti in giudizio, **interesse pubblico rilevante**, medicina e sanità, sanità pubblica, ricerca/archiviazione). → *"Sempre" è un assoluto: diffidarne.* |
| **4** ∅ | Inglese, comprensione | — | *"It must finish looking at the report and receive everything it asked for"*: il testo dice *"can decide… only after it has finished its checks"* |
| **8** ∅ | DPCM 1/10/2012, abbinamento errato | — | **"Casa Italia"** non si occupa di pari opportunità (è la funzione del **Dipartimento per le pari opportunità**, art. 16). Casa Italia (art. 12-bis) cura territorio, aree urbane e **patrimonio abitativo** (sicurezza ed efficienza energetica degli edifici). Gli altri abbinamenti erano corretti: Coordinamento amministrativo → **Commissione per l'accesso ai documenti** (art. 29); UCI trasparenza e integrità → performance (art. 31); Personale (art. 34). |
| **12** ❌ | Isolamento SQL | READ COMMITTED | **SERIALIZABLE**: è l'unico livello standard che impedisce le **phantom read** e le anomalie di serializzazione. READ COMMITTED impedisce solo le *dirty read*; il "distrattore" attribuiva lo snapshot stabile a READ COMMITTED (è falso). |
| **22** ∅ | Riserve di budget | — | **Contingency reserve** = rischi **identificati** (*known-unknowns*), **dentro la cost baseline**, gestita dal **PM**. **Management reserve** = rischi **non previsti** (*unknown-unknowns*), **fuori dalla baseline** ma dentro il **budget totale (BAC + MR)**, si usa **con l'approvazione** di sponsor e governance. |
| **24** ∅ | PNRR M1C1, semplificazione | — | I dati di **SUAP e SUE** sono resi accessibili sulla piattaforma **"Impresa in un giorno"** (Unioncamere/InfoCamere; misura di semplificazione e digitalizzazione delle procedure, M1C1 – Asse 2). |
| **33** ❌ | Art. 15 c.4 D.Lgs. 36/2023 | una fase per ciascun responsabile | Il RUP resta **unico**; nei modelli organizzativi si può nominare **un responsabile di procedimento per programmazione, progettazione ed esecuzione** e **un altro per la fase di affidamento** (2 responsabili, non 4). |
| **37** ∅ | CCB programma vs progetto | — | I **CCB di progetto** decidono le modifiche con impatto **locale**; **escalano** al **CCB di programma** quelle che toccano interdipendenze, budget di programma o **mappa dei benefici** (principio di governance per **soglie/tolleranze**, come la *gestione per eccezioni* di PRINCE2). |
| **38** ❌ | Refactoring | "riscrittura in un altro linguaggio" | **Modifica della struttura interna senza alterare il comportamento esterno** (Fowler): migliora leggibilità e manutenibilità e riduce il debito tecnico; è protetta dai **test di regressione**. La riscrittura in un altro linguaggio è un *rewrite* o una *migrazione*. |
| **42** ∅ | Data mart dipendente | — | **Sottoinsieme curato del DWH** per un ambito specifico (es. vendite, personale). È *dipendente* perché è alimentato dal DWH centrale (modello Inmon); il data mart **indipendente** si alimenta direttamente dalle fonti (Kimball "bus"). |
| **43** ∅ | Resource leveling | — | Il livellamento dà priorità al **vincolo della risorsa** e quindi **può allungare il percorso critico** → servono **ri-baseline formale** dei tempi. Il *resource smoothing* invece usa solo il float, senza toccare le date. |
| **47** ∅ | PNRR M1C1 Riforma 1.1 | — | **"Fast track"**: approccio semplificato per gli acquisti TIC del PNRR (white list di fornitori, procedure accelerate con Consip). |
| **57** ∅ | DPCM 1/10/2012 art. 12 | — | **Dipartimento per gli affari regionali e le autonomie**: segreteria della **Conferenza Stato-Regioni**; il suo Capo è segretario della **Conferenza unificata**. La **Conferenza Stato-città** ha un proprio Ufficio di segreteria (art. 27). |
| **58** ❌ | Art. 116 D.Lgs. 36/2023, affermazione NON corretta | quella sulla verifica durante l'esecuzione dei contratti periodici | L'affermazione **errata** era: *"per servizi e forniture ad elevato contenuto tecnologico la SA è tenuta a nominare verificatori diversi da RUP e DEC"*. Non c'è un **obbligo** generalizzato in questo senso; tutte le altre affermazioni riproducevano l'art. 116. → *Con le domande "NON corretta", cerca l'affermazione con un obbligo assoluto.* |

## 4. Che cosa dice la prova sulla commissione A (utile per l'orale)
1. **Program management** è il cuore del profilo: 8 quesiti su 40, con lessico **MSP/PMI** (*Program Benefits Charter, Benefits Realization Plan, Sponsoring Group, Program Board, OCM/ADKAR, Communications Management Plan*). Aspettati all'orale **un caso di programma PNRR** da governare.
2. Le norme sono chieste **per articolo** (art. 15 c.4 e art. 116 del Codice; artt. 12 e 29 del DPCM 2012; art. 14 GDPR) → serve **precisione**, non solo i concetti.
3. Le domande tecniche sono **applicative** (scenario → soluzione: SNMPv3, VPN site-to-site, SLAAC, VLAN + firewall, multi-AZ, ELT). All'orale funzionerà lo stesso schema: **"che cosa faresti se…"**.
4. I situazionali premiano: **documentare, coinvolgere i competenti, proporre opzioni graduate, verificare i risultati, non sostituirsi** a chi ha la competenza (privacy, contratti). Tu hai preso 12/12: **usa lo stesso stile nelle risposte all'orale**.

## 5. Punteggio finale e obiettivo dell'orale
**Graduatoria = titoli (max 60) + scritto (43,5) + orale (max 60, minimo 42).**
Ogni punto dell'orale pesa quanto un punto dello scritto: l'obiettivo realistico è **≥ 50/60**, ottenibile con la sicurezza sulle materie normative e con risposte strutturate.
