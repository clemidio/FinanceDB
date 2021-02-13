$(document).ready( function () {
  $('#myTable1').DataTable();
  $('#TransactionsTable').DataTable();
  $('#AssetsTable').DataTable();
  
  $('#AssetsTable1').DataTable({
    "processing": true,
    "serverSide": true,
    "ajax": "/asset/json/", 
    "columns": [
      {"data": "sigla"},
      {"data": "name"},
      {"data": "price"},
      {"data": "classe"},
      {"data": "setor"},
      {"data": "subsetor"},
      {"data": "segmento"}
    ]
  });
  $('#TransactionsTable1').DataTable({
    "processing": true,
    "serverSide": true,
    "ajax": "/transaction/json/", 
    "columns": [
      {"data": "operation"},
      {"data": "id"},
      {"data": "asset"},
      {"data": "date"},
      {"data": "amount"},
      {"data": "price"},
      {"data": "account_bank"},
      {"data": "nota_id"}
    ]
  });
  // $('#myTable2').DataTable({
  //   "ajax": "/person/json/",
  //   "columns": [
  //     {"data": "name"},
  //     {"data": "email"},
  //     {"data": "phone"},
  //     {"data": "gender"}
  //   ]
  // });
});