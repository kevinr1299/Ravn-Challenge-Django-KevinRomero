import { Component } from '@angular/core';
import { Router } from '@angular/router';

import { PeopleSource } from 'src/app/datasources/peopleSource';
import { Person } from 'src/app/interfaces/people';
import { PersonService } from 'src/app/services/person.service';

@Component({
  selector: 'app-side-bar',
  templateUrl: './side-bar.component.html',
  providers: [],
  styleUrls: ['./side-bar.component.scss'],
})
export class SideBarComponent {

  dataSource!: PeopleSource;
  personSelected: string = '';

  constructor(
    private personService: PersonService,
    private router: Router,
  ) {
    this.dataSource = new PeopleSource(
      this.personService,
    );
  }

  changeSelectPerson(person: Person) {
    this.personSelected = person.url;
    this.personService.setCurrentPerson(person);
    this.router.navigate(['person']);
  }
}
