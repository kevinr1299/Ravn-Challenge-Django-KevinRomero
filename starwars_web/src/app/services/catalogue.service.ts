import { HttpClient, HttpResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Catalogue } from '../interfaces/catalogue';

@Injectable({
  providedIn: 'root'
})
export class CatalogueService {

  constructor(private http: HttpClient) { }

  getCatalogue(url: string): Observable<Catalogue>{
    return this.http.get<Catalogue>(url);
  }
}
