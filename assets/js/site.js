// Expand/collapse abstract & media panels under each citation.
document.addEventListener('click', function(e){
  var btn = e.target.closest('[data-toggle]');
  if(!btn) return;
  var key = btn.getAttribute('data-toggle');
  var entry = btn.closest('.entry');
  if(!entry) return;
  var panel = entry.querySelector('.panel[data-panel="'+key+'"]');
  if(!panel) return;
  panel.classList.toggle('open');
});
