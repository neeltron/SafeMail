$(document).ready(function () {
  $("[data-bss-chart]").each(function (a, t) {
    this.chart = new Chart($(t), $(t).data("bss-chart"));
  });
});
