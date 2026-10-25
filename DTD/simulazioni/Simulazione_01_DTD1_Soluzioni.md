# Simulazione 01 DTD1 — Soluzioni commentate

## Griglia rapida
| Blocco A | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|
| 1 **b** | 2 **a** | 3 **c** | 4 **a** | 5 **b** | 6 **b** | 7 **a** | 8 **b** | 9 **c** | 10 **c** |
| 11 **b** | 12 **c** | 13 **a** | 14 **b** | 15 **c** | 16 **a** | 17 **b** | 18 **b** | 19 **c** | 20 **a** |
| 21 **b** | 22 **c** | 23 **a** | 24 **b** | 25 **a** | 26 **c** | 27 **b** | 28 **a** | 29 **c** | 30 **a** |
| 31 **b** | 32 **b** | 33 **c** | 34 **a** | 35 **c** | 36 **b** | 37 **a** | 38 **b** | 39 **c** | 40 **a** |

| Blocco B (più efficace / neutra / meno efficace) |
|---|
| 41 **b** / a / c · 42 **a** / c / b · 43 **c** / b / a · 44 **b** / c / a · 45 **a** / c / b · 46 **b** / c / a |
| 47 **c** / b / a · 48 **b** / a / c · 49 **b** / c / a · 50 **a** / c / b · 51 **c** / b / a · 52 **c** / b / a |

| Blocco C | | | | | | | |
|---|---|---|---|---|---|---|---|
| 53 **b** | 54 **b** | 55 **a** | 56 **b** | 57 **a** | 58 **a** | 59 **b** | 60 **b** |

## Calcolo del punteggio
`Punteggio = (corrette A + corrette C) − 0,5 × (errate A + errate C) + B`, dove B = n. più efficaci × 1 + n. neutre × 0,375. **Soglia 42.**

## Commenti al Blocco A
1. **CPI = EV/AC = 80/100 = 0,80** (< 1 → sovracosto). L'opzione c) calcola invece l'**SPI** = EV/PV = 0,89. → `studio/04` §1.
2. Percorso critico = il **più lungo**, con **float nullo**. Costi e risorse sono distrattori.
3. a) confonde "grande progetto" e programma; b) descrive il **portfolio**.
4. **Un solo Accountable** per attività; più "R" sono ammessi.
5. Il **Product Owner** gestisce il backlog; lo Scrum Master facilita.
6. **RPO = perdita di dati** tollerata; a) è l'**RTO**; c) è lo SLA di disponibilità.
7. /26 → 2^6 = 64 indirizzi − rete − broadcast = **62**.
8. **BGP** (protocollo EGP, *path vector*). OSPF e RIP sono protocolli interni (IGP).
9. I container condividono il **kernel** dell'host; le opzioni a) e b) invertono le caratteristiche.
10. **SaaS**: il fornitore gestisce tutto lo stack, fino all'applicazione.
11. **WHERE → righe, HAVING → gruppi**.
12. a) = Atomicità; b) = Isolamento; c) = **Durabilità**.
13. Molte relazioni complesse → **graph DB** (es. Neo4j).
14. Data lake = dati **grezzi**, **schema-on-read**.
15. 401 = **non autenticato**; **403 = autenticato ma non autorizzato**.
16. **PUT** è idempotente e sostituisce l'intera risorsa; PATCH la modifica in parte; POST non è idempotente.
17. Ricerca binaria **O(log n)** su una collezione **ordinata**.
18. Le PA devono rispettare **WCAG 2.1 livello AA** (EN 301 549, Linee guida AgID sull'accessibilità).
19. c) = **overriding** (polimorfismo dinamico); a) = **overloading**; b) = incapsulamento.
20. **Precision = TP/(TP+FP)**; b) = recall; c) = accuracy.
21. **RAG** = recupero di documenti + generazione: riduce le allucinazioni e fonda la risposta su fonti.
22. AI Act, All. III, punto 5: accesso a **servizi pubblici essenziali** → **alto rischio**. Il social scoring è invece vietato.
23. a) overfitting; b) underfitting.
24. Art. 50 D.Lgs. 36/2023: servizi e forniture **< 140.000 €**; lavori < 150.000 €. 40.000 € era la soglia del vecchio codice (D.Lgs. 50/2016).
25. RUP = Responsabile **Unico del Progetto** (art. 15).
26. BDNCP → **ANAC** (art. 23).
27. Art. 1: principio del **risultato**, criterio prioritario della discrezionalità.
28. Dialogo competitivo (art. 74): la SA **non sa definire** la soluzione; c) è il caso della negoziata senza bando (art. 76).
29. Art. 33 GDPR: **72 ore**; le 24 h della a) riguardano il pre-allarme NIS2.
30. Art. 37: DPO **obbligatorio** per autorità e organismi pubblici, eccetto le autorità giurisdizionali.
31. I dati pseudonimizzati **restano dati personali** (art. 4 n. 5 e considerando 26).
32. NIS2: **24 h** pre-allarme, 72 h notifica, 1 mese relazione finale.
33. **Zero Trust**: nessuna fiducia implicita, verifica continua, minimo privilegio.
34. **Reg. (UE) 2021/241** (RRF); b) è il GDPR, c) la NIS2.
35. **1.3.1 = PDND**; 1.2 = cloud dei Comuni; 1.7.2 = facilitazione.
36. **DNSH = Do No Significant Harm** agli obiettivi ambientali (Reg. 2020/852).
37. **Milestone qualitative / target quantitativi**.
38. Testo dell'art. 95, c.1 Cost. La nomina dei Ministri spetta al **Presidente della Repubblica**, su proposta del PdC (art. 92).
39. **DPCM 19/06/2019**. La L. 400/1988 regola la PCM in generale; il D.Lgs. 82/2005 è il CAD.
40. Art. 9 L. 400/1988: funzioni **delegate dal PdC**; i Ministri senza portafoglio **partecipano** al CdM.

## Commenti al Blocco B
- **41**: b) affronta il problema alla radice (FAQ, webinar), è scalabile e orientata all'utente; a) è diligente ma inefficiente (neutra); c) è un rifiuto del servizio.
- **42**: a) tutela gli SLA con evidenze e i ruoli contrattuali (DEC/RUP); c) è passiva; b) accetta una non conformità.
- **43**: c) dissenso tecnico motivato, con alternative e tracciabilità; b) blocca e scavalca la linea gerarchica (neutra); a) è acquiescente su un rischio di sicurezza.
- **44**: b) sviluppo del collega e controllo di qualità; c) informa ma senza supporto; a) nasconde il problema e non lo risolve.
- **45**: a) interoperabilità secondo le norme (PDND, ModI); c) passiva; b) soluzione insicura e non conforme.
- **46**: b) bilancia qualità, norme e tempi, con escalation; c) rigida ma tutela gli utenti; a) viola gli obblighi di accessibilità.
- **47**: c) gestione costruttiva del conflitto; b) evita il conflitto; a) lo fa degenerare.
- **48**: b) contenimento + segnalazione + prevenzione; a) parziale; c) diffonde la minaccia.
- **49**: b) decisione basata sui dati (art. 68 CAD, TCO, lock-in); c) la direzione è giusta ma manca la motivazione; a) ignora rischi e norme.
- **50**: a) verifica il dato prima di agire (uso delle informazioni); c) attendista; b) allarmismo senza verifica.
- **51**: c) preparazione + rete + restituzione; b) presenza passiva; a) evitamento.
- **52**: c) privacy by design; b) rifiuta, ma con una motivazione sbagliata (neutra); a) viola il principio di minimizzazione.

## Commenti al Blocco C
- 53: *provided that the migration is completed and verified* → b. 54: *unless the delay is caused by circumstances beyond their control* → b.
- 55: *beyond one's control* = fuori dalla propria possibilità d'intervento.
- 56: *since* + azione che dura fino ad oggi → **present perfect continuous**.
- 57: primo condizionale → *If + present, will*.
- 58: *tender* = gara/bando. 59: *comply with* = conformarsi a. 60: divieto → ***mustn't*** (*don't have to/needn't* = non è necessario).
