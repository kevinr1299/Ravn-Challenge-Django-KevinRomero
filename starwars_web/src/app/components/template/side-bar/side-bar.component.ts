import { Component, ChangeDetectionStrategy } from '@angular/core';

import { PeopleSource } from 'src/app/datasources/peopleSource';
import { PersonService } from 'src/app/services/person.service';

@Component({
  selector: 'app-side-bar',
  templateUrl: './side-bar.component.html',
  providers: [],
  styleUrls: ['./side-bar.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class SideBarComponent {

  dataSource!: PeopleSource;

  constructor(
    private personService: PersonService,
  ) {
    this.dataSource = new PeopleSource(this.personService);
   }
}
