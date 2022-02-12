import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PersonCellComponent } from './person-cell.component';

describe('PersonCellComponent', () => {
  let component: PersonCellComponent;
  let fixture: ComponentFixture<PersonCellComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PersonCellComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PersonCellComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
