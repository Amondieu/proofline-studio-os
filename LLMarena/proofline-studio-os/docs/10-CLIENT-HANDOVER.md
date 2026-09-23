# 10 — Client Handover
<!-- v0.1 · 2026-09-23 · owner: agent drafts, founder signs · completed copy lives in templates/handover-packet.md -->

## Ownership model (non-negotiable)
Repo · hosting · domain · analytics · CMS · content · form records → **client accounts**. We hold delegated access and remove ourselves on request. The final invoice is only issued once the client has proven their own access.

## Handover checklist
1. **Accounts**: client is the owner of record for registrar, DNS, hosting, GitHub org/repo, analytics, CMS, booking, form endpoint.
2. **Access**: we keep collaborator access until the support window ends, then it is revoked in writing.
3. **Credentials**: exchanged through the client's password manager or a one-time link — never email, never chat.
4. **Repo**: transferred (or a fresh repo created under their org) with README, ADRs and the launch receipt; `main` protected; deploy key from *their* account.
5. **Documentation**: how to edit content, how to add a page, how to publish, how to roll back, how to read analytics, what breaks what.
6. **Training**: 30-minute screen recording + one live session (tier 2/3); tier 1 gets the recording only.
7. **Data**: form records exported to the client; our copies deleted within the retention window; DPAs/processor notes attached.
8. **Backups**: export of the repo + content + database; restore instruction tested once.
9. **Analytics baseline**: 30-day pre/post numbers documented; no guarantees attached.
10. **Support window**: 14 days of defect fixes free (our bugs); everything else is a change request or a retainer.

## Maintenance options (ethical, priced, opt-in)
| Option | Price | Includes | Excludes |
|---|---|---|---|
| Care (light) | €60/mo | monthly dependency/security check, uptime + form monitoring, 1 small content change, quarterly performance report | new sections, redesigns |
| Care (active) | €140/mo | above + 2 h of improvements/month, quarterly CWV + accessibility re-check, priority response | campaigns, new pages |
| Project retainer | €500+/mo | agreed roadmap of work | open scope |
No auto-renewal traps; cancel any time with 30 days' notice; the client keeps everything either way.
