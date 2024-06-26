import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage implements OnInit {
  private apiUrlCampus = 'http://127.0.0.1:8000/main/api/campus/';
  private apiUrlCurso = 'http://127.0.0.1:8000/main/api/curso/';
  private apiUrlAluno = 'http://127.0.0.1:8000/main/api/aluno/';

  cursos: any[] = [];
  campi: any[] = [];
  alunos: any[] = [];

  constructor(private http: HttpClient) {}

  getCampus(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrlCampus);
  }

  getCurso(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrlCurso);
  }

  getAluno(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrlAluno);
  }

  ngOnInit() {
    this.loadItems();
  }

  loadItems() {
    this.getCampus().subscribe(data => {
      this.campi = data;
    });

    this.getCurso().subscribe(cursos => {
      this.cursos = cursos;
    });

    this.getAluno().subscribe(data => {
      this.alunos = data;
    });
  }

}
