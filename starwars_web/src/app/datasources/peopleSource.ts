import { CollectionViewer, DataSource } from '@angular/cdk/collections';
import { BehaviorSubject, Observable, Subscription } from 'rxjs';

import { Person } from 'src/app/interfaces/people';
import { PersonService } from 'src/app/services/person.service';

export class PeopleSource extends DataSource<Person | undefined> {
    private _pageSize = 5;
    private _cachedData = Array.from<Person>([]);
    private _fetchedPages = new Set<number>();
    private _max = 0;
    private _current = this._pageSize;
    private readonly _dataStream = new BehaviorSubject<(Person | undefined)[]>(this._cachedData);
    private readonly _subscription = new Subscription();

    constructor(private personService: PersonService) {
        super();
        this.call_api(1);
    }

    connect(collectionViewer: CollectionViewer): Observable<(Person | undefined)[]> {
        this._subscription.add(
            collectionViewer.viewChange.subscribe(range => {
                const startPage = this._getPageForIndex(range.start);
                const endPage = this._getPageForIndex(range.end - 1);
                if (this._current < this._max) {
                    for (let i = startPage; i <= endPage; i++) {
                        this._fetchPage(i + 2);
                    }
                }
            }),
        );
        return this._dataStream;
    }

    disconnect(): void {
        this._subscription.unsubscribe();
    }

    private call_api(page: number) {
        this.personService.getPeople(page).subscribe(
            response => {
                this._fetchedPages.add(page);
                this._cachedData = response.body!.results;
                this._max = response.body!.count;
                this._dataStream.next(this._cachedData);
            }
        )
    }

    private _getPageForIndex(index: number): number {
        return Math.floor(index / this._pageSize);
    }

    private _fetchPage(page: number) {
        if (this._fetchedPages.has(page)) {
            return;
        }
        this._fetchedPages.add(page);
        this._current += this._pageSize;

        this.personService.getPeople(page).subscribe(
            (response) => {
                this._cachedData = this._cachedData.concat(response.body!.results)
                this._dataStream.next(this._cachedData);
            },
            error => {
                this.disconnect()
            }
        )
    }
}