# Sintesi: Normazione Tecnica e Modelli di Interoperabilità

Sintesi mirata alle **Materie 1 e 2** del bando AGID-01 (art. 7) — corrispondenti al **Ramo A** della [mappa mentale del concorso](Mappa_Mentale_AGID.html). Fonti: `AGID/Pubblicazioni_e_Linee_Guida_AGID.md` §1-2, `AGID/pdf/03-06` e `21`.

---

## 1. Normazione Tecnica Nazionale, Comunitaria e Internazionale

*   **Standard tecnici richiamati dal Modello di Interoperabilità (ModI)**: TLS 1.2/1.3, OAuth 2.0, OpenID Connect, OAS3/OpenAPI, X.509, XML Canonicalization/Digest/Signature — fonte `AGID/pdf/05`.
*   **Normativa comunitaria di riferimento**:
    *   **eIDAS** (Reg. UE 910/2014): identità digitale e servizi fiduciari transfrontalieri, base delle firme elettroniche del CAD.
    *   **Direttiva 2014/55/UE**: fatturazione elettronica nella PA, veicolata via rete **PEPPOL** (di cui AGID è **Authority nazionale**).
    *   **GDPR** (Reg. UE 2016/679): protezione dei dati personali, trasversale a tutte le materie che trattano dati.
    *   **AI Act** (Reg. UE 2024/1689): classificazione del rischio dei sistemi di IA (vedi `Sintesi_Dati_Metadatazione_ML.md`).
*   **Attuazione nazionale**: Circolare AGID 2/2019 (standard NormeInRete per il patrimonio informativo giuridico); Regole Tecniche PAD v2 (`AGID/pdf/21`) per l'e-procurement.
*   **Enti di normazione internazionale**: ISO/IEC, ETSI, IETF (RFC), W3C, OASIS — AGID partecipa come nodo nazionale di raccordo (es. PEPPOL Authority).
*   **Accessibilità come standard tecnico**: WCAG 2.1 / EN 301 549, recepiti a livello nazionale dall'EAA (European Accessibility Act, D.Lgs. 82/2022).

> **Perché rilevante per un esame tecnico-normativo**: questa materia è la "cornice" delle altre — ogni volta che si cita uno standard applicativo (OAuth, mTLS, DCAT) va ricondotto alla fonte normativa che lo rende vincolante per la PA (norma tecnica internazionale → direttiva/regolamento UE → attuazione AGID).

---

## 2. Modelli di Interoperabilità (ModI & PDND)

*   **ModI**: regole tecniche AGID per lo scambio dati tra sistemi della PA via API REST e SOAP (`AGID/pdf/03-04`), articolate in 4 allegati:
    1.  **Pattern di interazione** — sincroni/asincroni, request-reply, pub-sub.
    2.  **Pattern di sicurezza** — autenticazione, autorizzazione, integrità.
    3.  **Profili di interoperabilità** — combinazioni tipizzate di pattern per casi d'uso ricorrenti.
    4.  **Raccomandazioni di implementazione** — linee guida pratiche per gli sviluppatori.
*   **Sicurezza delle API** (`AGID/pdf/05`): autenticazione tramite certificati **X.509** e **mTLS** server-to-server; autorizzazione tramite **OAuth 2.0**. I due meccanismi sono complementari — mTLS prova *chi è* il sistema chiamante, OAuth 2.0 prova *cosa può fare*.
*   **PDND — Piattaforma Digitale Nazionale Dati** (`AGID/pdf/06`): infrastruttura di interoperabilità che funge da **control-plane/broker di fiducia** (non un data lake centrale — i dati non transitano da PDND). Concetti chiave: **Catalogo E-Service**, **adesione** degli enti, **voucher** (token a breve durata per l'accesso), gestione **eventi** e **scambio dati asincrono**.
*   **Principio cardine — Once Only**: nessuna PA può richiedere al cittadino/impresa dati già in possesso di un'altra PA; l'interoperabilità tecnica (ModI/PDND) è lo strumento abilitante di questo principio giuridico-organizzativo, richiamato anche dal Piano Triennale (materia 7) e dal FVOE nel Codice Appalti (materia 9).

---

## Mappa dei collegamenti con le altre materie del bando

| Materia 1-2 (questo documento) | Collegata a |
|---|---|
| eIDAS, firme elettroniche | Materia 12 — CAD (FES/FEA/FEQ) |
| PEPPOL, fatturazione elettronica | Materia 9 — Gare pubbliche ICT / e-procurement |
| OAuth 2.0, mTLS, X.509 | Materia 4 — Architetture applicative (sviluppo sicuro / Secure by Design) |
| PDND, Once Only | Materia 3 — Modellazione dati (OntoPiA, DCAT-AP_IT per la semantica dei dati scambiati) |
| AI Act | Materia 3 — Machine Learning nella PA |
