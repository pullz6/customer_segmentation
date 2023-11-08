import { Component, OnInit } from '@angular/core';
import { Customer } from "src/app/Customer";
import { CUSTOMERS } from "src/app/mock_customers";

@Component({
  selector: 'app-customer',
  templateUrl: './customer.component.html',
  styleUrls: ['./customer.component.css']
})
export class CustomerComponent implements OnInit {
  customers: Customer[] = CUSTOMERS;

  constructor(){}

  ngOnInit():void{}
}
