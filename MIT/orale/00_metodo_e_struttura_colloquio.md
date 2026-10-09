# Metodo per la Prova Orale — Concorso MIT-EPI (Specialista Informatico)

## Struttura della prova (art. 7 del bando)
1. **Colloquio interdisciplinare** sulle stesse 12 materie della prova scritta — non quiz a risposta multipla, ma domande aperte/discorsive.
2. **Conversazione in lingua inglese** (livello atteso: almeno B2).
3. **Accertamento delle competenze digitali** (uso di strumenti/tecnologie ICT).

Punteggio massimo 30, soglia di superamento **21/30**, come per lo scritto.

---

## Come strutturare ogni risposta (schema in 5 punti)
Per domande tecniche aperte, rispondi seguendo questo schema — dà ordine al discorso e tocca automaticamente i punti che una commissione tecnica si aspetta:

1. **Definizione chiara e concisa** del concetto/tecnologia richiesta (una frase, senza divagare).
2. **Come funziona / meccanismo tecnico** — il "come", non solo il "cosa".
3. **Esempio pratico o caso d'uso**, idealmente calato nel contesto delle infrastrutture/trasporti/PA (il MIT gestisce ponti, ferrovie, strade, trasporto aereo/marittimo, digitalizzazione della PA) — mostra che sai collegare la teoria al dominio dell'amministrazione.
4. **Trade-off, limiti o criticità** — nessuna soluzione tecnica è priva di compromessi; nominarli mostra maturità ingegneristica (coerente con la persona "Senior Solutions Architect / Security Chief" richiesta dal ruolo).
5. **Collegamento normativo o di sicurezza**, se pertinente (GDPR, NIS2, CAD, Zero Trust, ecc.) — per un ente pubblico, la conformità non è un dettaglio accessorio.

Non serve applicare tutti e 5 i punti a ogni domanda (una domanda molto specifica, es. "cosa fa `systemctl enable`", richiede solo i punti 1-2), ma per domande ampie ("come progetteresti...", "cosa sono...") questo schema evita risposte disordinate o troppo brevi.

## Tarare il registro sul profilo della commissione (vedi `analisi_commissione_epi.md`)
- **Prof. Pinna (Presidente, informatica teorica/metodi formali — confermato):** apprezzerà risposte che **argomentano la correttezza**, non solo l'efficacia ("perché questa soluzione è corretta", non solo "perché funziona"). Se la domanda riguarda un algoritmo/architettura, è utile menzionare esplicitamente invarianti, casi limite, o perché un approccio è preferibile in termini logici/strutturali, non solo prestazionali.
- **Profilo di sicurezza (claim su Agrifoglio non confermato, ma la materia 7 è comunque centrale nel bando):** mantieni sempre un'ottica Security-First quando pertinente — non serve esagerare, ma non va mai ignorata se la domanda tocca architetture/dati.
- **Ruolo dati/statistica (Ing. Lazzaretti, confermato):** se la domanda riguarda dati, big data, BI, è utile mostrare consapevolezza dell'intera catena dato→informazione→decisione, non solo l'algoritmo isolato.
- **In generale:** la commissione valuta un profilo "Specialista Informatico" per una PA — rispondi sempre pensando "come lo spiegherei/applicherei in un contesto reale del MIT", non in astratto.

## Errori da evitare
- Rispondere con un elenco di parole chiave senza legarle in un discorso coerente.
- Dare solo la definizione (punto 1) senza mai arrivare a un esempio o a un trade-off — rischia di sembrare una risposta "mandata a memoria" senza comprensione.
- Ignorare completamente l'aspetto normativo quando la domanda lo richiede implicitamente (es. parlare di un sistema che tratta dati personali senza mai citare il GDPR).
- Essere troppo lunghi su domande semplici: se la domanda è puntuale (es. "differenza tra TCP e UDP"), una risposta di 30 secondi ben strutturata vale più di 3 minuti dispersivi.

---

## Colloquio in lingua inglese
Vedi [`01_english_conversation_prep.md`](01_english_conversation_prep.md) per domande tipiche e vocabolario tecnico.

## Competenze digitali
La verifica delle competenze digitali nella prova orale è tipicamente integrata nel colloquio tecnico stesso (dato il profilo "Specialista informatico", l'intera prova è già una verifica di competenze digitali) — non richiede una preparazione separata oltre al ripasso delle 12 materie in `MIT/studio/`.
