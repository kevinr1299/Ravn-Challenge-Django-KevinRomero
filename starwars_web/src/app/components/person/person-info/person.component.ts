import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { Person } from 'src/app/interfaces/people';
import { CatalogueService } from 'src/app/services/catalogue.service';
import { PersonService } from 'src/app/services/person.service';

@Component({
  selector: 'app-person',
  templateUrl: './person.component.html',
  styleUrls: ['./person.component.scss'],
})
export class PersonComponent implements OnInit {

  person: Person | null = null;
  vehicles: string[] = [];

  constructor(
    private personService: PersonService,
    private catalogueService: CatalogueService,
  ) { }

  ngOnInit(): void {
    this.personService.getCurrentPerson().subscribe({
      next: person => {
        this.person = person
        this.vehicles = [];
        person?.vehicles.forEach(vehicle => {
          this.catalogueService.getCatalogue(vehicle).subscribe({
            next: data => this.vehicles.push(data.name),
          })
        })
      },
    })
  }
}
