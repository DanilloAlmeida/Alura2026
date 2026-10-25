import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-listar-pensamento',
  templateUrl: './listar-pensamento.component.html',
  styleUrls: ['./listar-pensamento.component.css']
})
export class ListarPensamentoComponent implements OnInit {

  listaPensamentos = [
    {
      conteudo: 'escrito em listar-pensamento',
      autoria: 'Nayane',
      modelo: 'modelo3'
    },
    {
      conteudo: 'escrito em listar-pensamento 2',
      autoria: 'Nayane 2',
      modelo: 'modelo2'
    },
    {
      conteudo: 'escrito em listar-pensamento 3',
      autoria: 'Nayane 3',
      modelo: 'modelo3'
    },
    {
      conteudo: 'escrito em listar-pensamento 4',
      autoria: 'Nayane 4',
      modelo: 'modelo1'
    }

  ];

  constructor() { }

  ngOnInit(): void {
  }

}
