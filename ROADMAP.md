# Rawdah – veikart

Ting vi har bestemt at skal komme, men som ikke er laget ennå. Oppdater lista når noe blir gjort.

## Viktigst: interaktiv del i Bayt al-Ḥikma (Visdommens hus)

Hver lærd i Visdommens hus skal etter hvert få en liten aktivitet. Bibliotekaren hinter allerede til disse i appen (`HTEASE` i `index.html`), så løftet er gitt til brukerne. En planlagt påminnelse kommer den 1. i hver måned.

- [ ] **al-Khwārizmī:** løs en enkel likning slik han gjorde, med kvadrater og rektangler («fullføre kvadratet»).
- [ ] **al-Jazarī:** se elefantklokka gå, med figurer som beveger seg hver halvtime.
- [ ] **Ibn al-Haytham:** mørkt rom med et lite hull, der bildet kommer opp ned (camera obscura).
- [ ] **al-ʻIjliyya:** sett sammen en astrolab og finn bønnetid eller qibla.
- [ ] **al-Bīrūnī:** mål jordas radius fra en fjelltopp (høyde + vinkel til horisonten).
- [ ] **Ibn Baṭṭūṭa:** følg reiseruten på et kart.
- [ ] De andre lærde: finn en idé per person.

## Innhold

- [ ] Flere lærde i Visdommens hus etter de 16 første.
- [x] Ibn Sīnā, al-Fārābī, Ibn Rushd og Ibn al-Bayṭār lagt til (med ærlig merknad om al-Ghazālīs kritikk).
- [ ] Påskeegg for resten av personene i Rihla-brevene.
- [ ] Oppdater muslimtallene i Rihla når Pew Research Center publiserer nyere tall (dagens tall er anslag for 2020, publisert 2025).

## Ramadan-oppdatering (før Ramadan 2027, ca. 8. februar)

- [ ] Ramadan-preg på hagen: lykter, halvmåne og iftār-stemning.
- [ ] Velvære i Ramadan: råd om suhūr og iftār i stedet for vann midt på dagen (vannpåminnelsen er allerede slått av i Ramadan).
- [ ] Egne vers og påminnelser for fasten, Laylat al-Qadr og de siste ti nettene.

## Funksjoner

- [ ] Pausedager (f.eks. ved sykdom eller reise) uten at hagen tar skade.
- [ ] Lyd uten nett (lagre resitasjonen lokalt).
- [ ] Bytte av «pass» eller stempler mellom brukere.
- [ ] Tilbakemeldingsknapp i appen (f.eks. lenke til et Google-skjema).
- [ ] Kreditering av oversettelser, resitatører og fonter; sjekk vilkår før appen spres bredt.
- [ ] Faglig gjennomlesning av vers, hadith og historiske tekster av en lærd.
- [ ] Ekte push-varsler (krever server, f.eks. OneSignal).

## Testversjoner (Rawdah Kahwa 7142)

- Testversjonene lages fra `index.html` med `python3 tools/build_kahwa.py`. Kjør skriptet etter hver endring i appen, ellers får testerne en gammel versjon.
- Ny tester: legg til et navn i `TESTERS` i skriptet. Hver tester får egen mappe (`kahwatest-<navn>/`), egen lagring og egen «tidsmaskin».
- Mannen med rosinhodet (al-Bukhārī 7142) finnes bare i testversjonene, ikke i hovedutgaven.
- Tilbakemeldinger: Google-skjemaet som er lenket i `TESTERS`.
