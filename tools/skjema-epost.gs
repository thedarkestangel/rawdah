// Rawdah: send hele skjemasvaret til deg på e-post hver gang noen svarer.
// 1) Lim inn alt dette i Apps Script fra skjemaet.  2) Velg «oppsett» og trykk Kjør én gang.

function oppsett() {
  const form = FormApp.getActiveForm();
  ScriptApp.getProjectTriggers().forEach(t => ScriptApp.deleteTrigger(t));
  ScriptApp.newTrigger('nyttSvar').forForm(form).onFormSubmit().create();
}

function nyttSvar(e) {
  const svar = e.response.getItemResponses();
  const tekst = svar.map(r => {
    let v = r.getResponse();
    if (Array.isArray(v)) v = v.map(x => Array.isArray(x) ? x.join(' / ') : x).join(', ');
    return '■ ' + r.getItem().getTitle() + '\n' + (v || '–');
  }).join('\n\n');
  const os = svar.length ? [].concat(svar[0].getResponse()).join(', ').slice(0, 40) : '';
  MailApp.sendEmail({
    to: Session.getEffectiveUser().getEmail(),
    subject: 'Rawdah: nytt skjemasvar' + (os ? ' (' + os + ')' : ''),
    body: tekst + '\n\nSendt ' + e.response.getTimestamp().toLocaleString('no-NO')
  });
}
