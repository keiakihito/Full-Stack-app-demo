import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { BaseService } from './base.service';

@Injectable({
  providedIn: 'root'
})
export class PlayersService extends BaseService {
  constructor(protected http: HttpClient) {
    super(http);
  }

  // Method for getting player summary by player ID
  getPlayerSummary(playerID: number): Observable<any> {
    const endpoint = `${this.baseUrl}/playerSummary/${playerID}`;

    return this.get(endpoint).pipe(map(
      (data: Object) => {
        return {
          endpoint: endpoint,
          apiResponse: data
        };
      },
      error => {
        return error;
      }
    ));
  }

  // Method for getting player suggestions by player name (autocomplete)
  autocompletePlayerName(partialName: string): Observable<any> {
    const endpoint = `${this.baseUrl}/autocomplete/${partialName}`; // This should match your Django URL pattern

    return this.get(endpoint).pipe(map(
      (data: Object) => {
        return data;  // Assuming the backend returns player name suggestions
      },
      error => {
        return error;
      }
    ));
  }

  // Method for getting autocomplete suggestions for player names
  getAutocompleteSuggestions(query: string): Observable<any> {
    const endpoint = `${this.baseUrl}/autocomplete/${query}`; // Adjust your backend path if needed

    return this.get(endpoint).pipe(map(
      (data: Object) => {
        return data;  // Assuming the backend returns a list of player names
      },
      error => {
        return error;
      }
    ));
  }


}
