import { Injectable } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { environment } from 'src/environments/environment';

import { People, Person } from '../interfaces/people';
import { BehaviorSubject, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PersonService {

  personURL = `${environment.api_url}/people/`
  private _currentPerson = new BehaviorSubject<Person | null>(null);

  constructor(private http: HttpClient) { }

  getPeople(page: number = 1): Observable<HttpResponse<People>>{
    return this.http.get<People>(
      `${this.personURL}?page=${page}`, {observe: 'response'}
    );
  }

  setCurrentPerson(person: Person) {
    this._currentPerson.next(person);
  }

  getCurrentPerson() {
    return this._currentPerson.asObservable();
  }
}
