import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';


@Injectable({
  providedIn: 'root'
})
export class NewsletterService {
  //TODO: Falta desarrollar backend
  private url: string = environment.apiUrl+'/api/newsletter/'

  constructor(private http: HttpClient) {
    console.log("*** Servicio Lista de correos corriendo ***")
  }

// metodo para registrar un nuevo email
postNewsletter(mail:string): Observable<any[]> {
  const formData = new FormData(); // objeto de tipo formdata
  formData.append('email', mail);
    return this.http.post<any[]>(this.url, formData);
  }
}