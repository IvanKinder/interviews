Ext.onReady(function () {
    Ext.define('Books', {
        extend: 'Ext.data.Model'
    });

    var store = Ext.create('Ext.data.Store', {
        model: 'Books',
        autoLoad: true,
        proxy: {
            type: 'rest',
            url: 'http://127.0.0.1:8080/books/',
            reader: {
                type: 'json'
            }
        }
    });

    Ext.create('Ext.grid.Panel', {
        title: 'Books',
        height: 900,
        width: 1400,
        store: store,
        columns: [{
            header: 'name',
            dataIndex: 'name'
        }, {
            header: 'author',
            dataIndex: 'author'
        }, {
            header: 'year',
            dataIndex: 'year'
        }, {
            header: 'in_stock',
            dataIndex: 'in_stock'
        }, {
            header: 'price',
            dataIndex: 'price'
        }],
        renderTo: Ext.getBody()
    });

    // Ext.create('Ext.Button', {
    //     text: 'Click me',
    //     margin: '-800 0 0 600',
    //     height: 90,
    //     width: 140,
    //     renderTo: Ext.getBody(),
    //     enableToggle: true
    // });
    var button = Ext.create('Ext.Button', {
        text: 'Button',
        margin: '-800 0 0 600',
        renderTo: Ext.getBody(),
        height: 90,
        width: 140,
        enableToggle: true,
        items: {
                xtype: 'button',
                text: 'My tton',
                badgeText: '2',
                handler: function () {
                    alert('tapped');
                }
            }
    });
});