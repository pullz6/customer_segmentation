import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import {HttpClientModule} from '@angular/common/http'

import { AppComponent } from './app.component';
import { HeaderComponent } from './components/header/header.component';
import { ButtonComponent } from './components/button/button.component';
import { CustomerComponent } from './components/customer/customer.component';
import { CustomerItemComponent } from './components/customer-item/customer-item.component';
import { AddCustomerComponent } from './components/add-customer/add-customer.component';


@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    ButtonComponent,
    CustomerComponent,
    CustomerItemComponent,
    AddCustomerComponent
  ],
  imports: [
    BrowserModule,
    FontAwesomeModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
