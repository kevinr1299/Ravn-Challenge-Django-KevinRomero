import { Component, Input } from '@angular/core';
import { Observable } from 'rxjs';
import { Person } from 'src/app/interfaces/people';
import { CatalogueService } from 'src/app/services/catalogue.service';

@Component({
  selector: 'app-person-cell',
  templateUrl: './person-cell.component.html',
  styleUrls: ['./person-cell.component.scss']
})
export class PersonCellComponent {

  @Input()
  person!: Person;
  @Input()
  selected: Boolean = false;
  specie = new Observable<string>(observer => {
    this.catalogueService.getCatalogue(this.person.specie).subscribe(
      data => {
        observer.next(data.name)
      }
    )
  })
  world = new Observable<string>(observer => {
    this.catalogueService.getCatalogue(this.person.homeworld).subscribe(
      data => {
        observer.next(data.name);
      }
    )
  })

  constructor(private catalogueService: CatalogueService) {
  }
}
