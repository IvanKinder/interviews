Ext.application({
    name: 'frontend',
    launch : function() {
        var win = Ext.create("Ext.window.Window", {
        title: 'My first window',
        width: 900,
        height: 600,
        maximizable: true,
        html: 'this is my first window'
        });
    win.show();
    }
});