import { Injectable } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { environment } from 'src/environments/environment';

import { People } from '../interfaces/people';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PersonService {

  personURL = `${environment.api_url}/people/`

  constructor(private http: HttpClient) { }

  getPeople(page: number = 1): Observable<HttpResponse<People>>{
    return this.http.get<People>(
      `${this.personURL}?page=${page}`, {observe: 'response'}
    );
  }
}
