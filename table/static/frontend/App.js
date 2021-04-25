Ext.onReady(function () {
    Ext.define('Books', {
        extend: 'Ext.data.Model'
    });

    var store = Ext.create('Ext.data.Store', {
        model: 'Books',
        autoLoad: true,
        proxy: {
            type: 'rest',
            url: 'http://127.0.0.1:8000/books/',
            reader: {
                type: 'json',
                root: 'data'
            },
            writer: {
                type: 'json',
                root: 'data'
            }
        }
    });

    var Editing = Ext.create('Ext.grid.plugin.RowEditing');


    Ext.create('Ext.grid.Panel', {
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
                xtype: 'textfield'
            }
        }, {
            header: 'in_stock',
            dataIndex: 'in_stock',
            field: {
                xtype: 'textfield'
            }
        }, {
            header: 'price',
            dataIndex: 'price',
            field: {
                xtype: 'textfield'
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
                    store.insert(0, new Books());
                    Editing.startEdit(0, 0);
                }
            },
            {
                itemId: 'delete',
                text: 'Delete',
                handler: function () {
                    var selection = grid.getView().getSelectionModel().getSelection()[0];
                    if (selection) {
                        store.remove(selection);
                    }
                }
            }],
        renderTo: Ext.getBody()
    });
});