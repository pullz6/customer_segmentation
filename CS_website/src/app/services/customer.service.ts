import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http'
import {Observable} from 'rxjs'
import { Customer } from "src/app/Customer";

@Injectable({
  providedIn: 'root'
})
export class CustomerService {

  private apiUrl = 'http://localhost:3030/Customers'

  constructor(private http:HttpClient) { }

  getCustomer(): Observable<Customer[]>{
    return this.http.get<Customer[]>(this.apiUrl)
  }

  deleteCustomer(customer : Customer): Observable<Customer> {
    const url = `${this.apiUrl}/${customer.id}`;
    return this.http.delete<Customer>(url)
  }
}
