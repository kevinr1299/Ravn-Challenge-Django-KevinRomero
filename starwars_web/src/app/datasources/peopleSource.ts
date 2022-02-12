import { CollectionViewer, DataSource } from '@angular/cdk/collections';
import { BehaviorSubject, Observable, Subscription } from 'rxjs';

import { Person } from 'src/app/interfaces/people';
import { PersonService } from 'src/app/services/person.service';

export class PeopleSource extends DataSource<Person | undefined> {

    hasError: Boolean = false;
    isLoading: Boolean = true;
    private _pageSize = 5;
    private _cachedData = Array.from<Person>([]);
    private _fetchedPages = new Set<number>();
    private _next: any;
    private _current = 0;
    private _last_end = 0;
    private readonly _dataStream = new BehaviorSubject<(Person | undefined)[]>(this._cachedData);
    private readonly _subscription = new Subscription();

    constructor(
        private personService: PersonService,
    ) {
        super();
        this.call_api(1);
    }

    connect(collectionViewer: CollectionViewer): Observable<(Person | undefined)[]> {
        this._subscription.add(
            collectionViewer.viewChange.subscribe(range => {
                const endPage = this._getPageForIndex(range.end);
                if (this._last_end < endPage) {
                    this._last_end = endPage;
                    if(this._next != null) this._fetchPage(this._current+1)
                }
            }),
        );
        return this._dataStream;
    }

    disconnect(): void {
        this._subscription.unsubscribe();
    }

    private call_api(page: number) {
        this.isLoading = true
        this.personService.getPeople(page)
        .subscribe({
            next: response => {
                this._current++;
                this._fetchedPages.add(page);
                this._cachedData = this._cachedData.concat(response.body!.results)
                this._next = response.body!.next;
                this._dataStream.next(this._cachedData);
            },
            error: () => {
                console.log(0)
                this.hasError = true;
                this.disconnect();
            },
            complete:  () => {
                this.isLoading = false;
            }
        })
    }

    private _getPageForIndex(index: number): number {
        return Math.floor(index / this._pageSize);
    }

    private _fetchPage(page: number) {
        if (this._fetchedPages.has(page)) {
            return;
        }
        this.call_api(page);
    }
}