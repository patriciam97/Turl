import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})
export class DatabaseService {
  baseUrl: String = 'http://localhost:4200';
  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
    }),
  };
  constructor(private httpClient: HttpClient) {}
  convert(longLink): void {
    let body = {
      link: longLink,
    };
    this.httpClient
      .post(this.baseUrl + '/urls/', body, this.httpOptions)
      .subscribe((res: {}) => {
        console.log(res);
      });
  }
}
