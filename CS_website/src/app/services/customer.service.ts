import { Injectable } from '@angular/core';
import {Observable, of} from 'rxjs'
import { Customer } from "src/app/Customer";
import { CUSTOMERS } from "src/app/mock_customers";

@Injectable({
  providedIn: 'root'
})
export class CustomerService {

  constructor() { }

  getCustomer(): Observable<Customer[]>{
    const customers = of(CUSTOMERS);
    return customers;
  }
}
