import { Component, OnInit } from '@angular/core';
import { Customer } from "src/app/Customer";
import { CustomerService } from "src/app/services/customer.service"

@Component({
  selector: 'app-customer',
  templateUrl: './customer.component.html',
  styleUrls: ['./customer.component.css']
})
export class CustomerComponent implements OnInit {
  customers: Customer[] = [];

  constructor(private customerService : CustomerService){}

  ngOnInit():void{
    this.customerService.getCustomer().subscribe((customers)=>this.customers = customers);
  }

  deleteCustomer(customer: Customer){
    this.customerService.deleteCustomer(customer).subscribe(()=>(this.customers = this.customers.filter((c) => c.id !== customer.id)));
  }

  toggleReminder(customer : Customer){
    console.log(124)
  }

}
