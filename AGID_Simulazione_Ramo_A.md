# Simulazione — Ramo A: Standard & Interoperabilità
### Concorso AGID-01 · Materie 1, 2 del bando (art. 7)

> **Formato.** Quesiti a risposta sintetica sul ramo Standard & Interoperabilità (normazione tecnica nazionale/comunitaria/internazionale + modelli di interoperabilità ModI/PDND). Da integrare progressivamente con altri quesiti man mano che emergono in fase di ripasso.
>
> Vedi anche la [mappa mentale del concorso] — ramo A — e `AGID_Simulazione_Ramo_E.md` per il formato del caso gestionale.

---

## Quesito sintetico — OAuth 2.0
### Materie 1 · 2 · ⏱ 15'

> Il candidato descriva sinteticamente il framework OAuth 2.0, i ruoli coinvolti e il flusso *Authorization Code* con PKCE, illustrando perché le Linee Guida AGID sulla sicurezza delle API richiedono di affiancarlo a **mTLS** nelle interazioni tra sistemi della Pubblica Amministrazione.

### Griglia di autocorrezione

| Punto da toccare | ✓ |
|---|---|
| Definisce OAuth 2.0 come framework di **autorizzazione**, non autenticazione (RFC 6749) | ☐ |
| Elenca i 4 ruoli: resource owner, client, authorization server, resource server | ☐ |
| Descrive il flusso Authorization Code + PKCE: redirect a `/authorize`, consenso, `authorization code`, scambio con `code_verifier` per l'`access_token` | ☐ |
| Spiega perché PKCE è ormai richiesto anche per client confidential (protezione dal furto del code) | ☐ |
| Distingue **access token** (OAuth 2.0, "cosa può fare il client") da **ID token** (OpenID Connect, "chi è l'utente"), citando OIDC in SPID come caso reale | ☐ |
| Collega al ModI: OAuth 2.0 prova lo scope autorizzato, **mTLS/X.509** prova l'identità del sistema PA chiamante → difesa in profondità contro il furto/replay di un token bearer | ☐ |
| Cita almeno un rischio e la relativa mitigazione (token bearer rubabile → scope minimi, TTL breve, revoca/introspection) | ☐ |

**Soglia orientativa:** 5/7 voci toccate = risposta solida per una domanda sintetica di questo tipo.

---

*(altri quesiti sintetici sul ramo A verranno aggiunti qui in fase di ripasso)*
