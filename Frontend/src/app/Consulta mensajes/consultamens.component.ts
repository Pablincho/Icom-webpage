import { Component } from '@angular/core';

@Component({
  selector: 'consulta-mensajes',
  templateUrl: './consultamens.component.html',
})
export class ConsultaMensajesComponent {
  public titulo: string;

  title = 'Consulta Mensajes';
  constructor(){
      this.titulo="Consulta de mensajes"
      console.log("Se cargó el componente 'consultamens.component'")
  }
}