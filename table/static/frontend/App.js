Ext.onReady(function () {
    Ext.define('Book', {
        extend: 'Ext.data.Model',
        fields: [
            {name: 'name', type: 'string'},
            {name: 'author', type: 'string'},
            {name: 'year', type: 'int'},
            {name: 'in_stock', type: 'boolean'},
            {name: 'price', type: 'int'}
        ]
    });

    var store = Ext.create('Ext.data.Store', {
        model: 'Book',
        autoLoad: true,
        proxy: {
            type: 'rest',
            // url: 'http://127.0.0.1:8000/books/',
            api: {
                read: 'http://127.0.0.1:8000/books/',
                write: 'http://127.0.0.1:8000/books/',
                update: 'http://127.0.0.1:8000/books/',
                destroy: 'http://127.0.0.1:8000/books/',
            },
            reader: {
                type: 'json',
                rootProperty: 'data'
            },
            writer: {
                type: 'json',
                // rootProperty: 'data'
            }
        }
    });

    var Editing = Ext.create('Ext.grid.plugin.RowEditing');

    var post_handler = function () {
        store.insert(0, new Book());
        Editing.startEdit(0, 0);
        button = document.getElementById("button-1038-btnInnerEl")
        button.onclick = function () {
            table_el = document.getElementById('tableview-1025').children[1].firstChild
            var new_book = []
            for (let i = 0; i < 5; i++) {
                new_book.push(table_el.querySelectorAll('td')[i].firstChild.childNodes[0].data)
            }
            var new_book_obj = {
                "name": new_book[0],
                "author": new_book[1],
                "year": new_book[2],
                "in_stock": new_book[3],
                "price": new_book[4],
            }
            console.log(new_book_obj)
            Ext.Ajax.request({
                url: 'http://127.0.0.1:8000/books/',
                success: console.log('success'),
                failure: console.log('fail'),
                jsonData: new_book_obj
            })
        };
    }

    var grid = Ext.create('Ext.grid.Panel', {
        title: 'Books',
        plugins: [Editing],
        height: 900,
        width: 600,
        store: store,
        columns: [{
            header: 'name',
            dataIndex: 'name',
            field: {
                xtype: 'textfield'
            }
        }, {
            header: 'author',
            dataIndex: 'author',
            field: {
                xtype: 'textfield'
            }
        }, {
            header: 'year',
            dataIndex: 'year',
            field: {
                xtype: 'numberfield'
            }
        }, {
            header: 'in_stock',
            dataIndex: 'in_stock',
            field: {
                xtype: 'checkbox'
            }
        }, {
            header: 'price',
            dataIndex: 'price',
            field: {
                xtype: 'numberfield'
            }
        }],
        bbar: new Ext.PagingToolbar({
            store: store,
            displayInfo: true,
            displayMsg: 'Показано  {0} - {1} из {2}'
        }),
        tbar: [
            {
                text: 'Insert',
                handler: function () {
                    post_handler()
                }
            },
            {
                itemId: 'save',
                text: 'Save',
                handler: function () {
                    console.log('popo')
                }
            },
            {
                itemId: 'delete',
                text: 'Delete',
                handler: function () {
                    var selection = grid.getView().getSelectionModel().getSelection()[0];
                    if (selection) {
                        store.remove(selection);
                        fetch(selection.data.url, {
                            method: 'DELETE',
                        })
                            .then(res => res.text())
                            .then(res => console.log(res))
                    }
                }
            },
        ],
        renderTo: Ext.getBody()
    });
});