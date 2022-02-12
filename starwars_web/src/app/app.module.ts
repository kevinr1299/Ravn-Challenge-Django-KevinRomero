import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HttpClientModule } from '@angular/common/http';
import { MaterialModule } from 'src/material.module';
import { FlexLayoutModule } from '@angular/flex-layout';

import { HeaderBarComponent } from './components/template/header-bar/header-bar.component';
import { SideBarComponent } from './components/template/side-bar/side-bar.component';
import { PersonComponent } from './components/page/person/person.component';
import { PersonCellComponent } from './components/page/person-cell/person-cell.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderBarComponent,
    SideBarComponent,
    PersonComponent,
    PersonCellComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MaterialModule,
    FlexLayoutModule,
    HttpClientModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
