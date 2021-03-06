from django.conf.urls import *
from AdminConsorcios.views import *
urlpatterns = patterns('',
 	url(r'^$',  inicio, name='inicio'),
	url(r'^registroExitoso/', 'AdminConsorcios.views.registroExitoso', name='registroExitoso'),
	url(r'^usuario/cerrarsesion/', 'AdminConsorcios.views.cerrarsesion', name='cerrarsesion'),
 	url(r'^usuario/registro/', 'AdminConsorcios.views.registro', name='registro'),
	url(r'^agregarReclamo/', 'AdminConsorcios.views.agregarReclamo', name='agregarReclamo'),
	url(r'^agregarFactura/', 'AdminConsorcios.views.agregarFactura', name='agregarFactura'),
	url(r'^agregarConsorcio/', 'AdminConsorcios.views.agregarConsorcio', name='agregarConsorcio'),
	url(r'^usuario/iniciarsesion/', 'AdminConsorcios.views.iniciarsesion', name='iniciarsesion'),
	url(r'^mostrarReclamo/', 'AdminConsorcios.views.mostrarReclamo', name='mostrarReclamo'),
	url(r'^mostrarConsorcio/', 'AdminConsorcios.views.mostrarConsorcio', name='mostrarConsorcio'),
	url(r'^mostrarFactura/', 'AdminConsorcios.views.mostrarFactura', name='mostrarFactura'),
	url(r'^modificarConsorcio/(?P<id>\d+)/$', 'AdminConsorcios.views.modificarConsorcio', name='modificarConsorcio'),	
	url(r'^modificarFactura/', 'AdminConsorcios.views.modificarFactura', name='modificarFactura'),
	url(r'^modificarReclamo/(?P<id>\d+)/$', 'AdminConsorcios.views.modificarReclamo', name='modificarReclamo'),
	url(r'^facturas/', 'AdminConsorcios.views.facturas', name='facturas'),	
	url(r'^consorcio/', 'AdminConsorcios.views.consorcio', name='consorcio'),
	url(r'^reclamo/', 'AdminConsorcios.views.reclamo', name='reclamo'),
	url(r'^agregarGasto/', 'AdminConsorcios.views.agregarGasto', name='agregarGasto'),
	url(r'^agregarAbono/', 'AdminConsorcios.views.agregarAbono', name='agregarAbono'),
	url(r'^agregarServicio/', 'AdminConsorcios.views.agregarServicio', name='agregarServicio'),
	url(r'^eliminarServicio/', 'AdminConsorcios.views.eliminarServicio', name='eliminarServicio'),
	url(r'^eliminarAbono/', 'AdminConsorcios.views.eliminarAbono', name='eliminarAbono'),
	url(r'^eliminarGasto/', 'AdminConsorcios.views.eliminarGasto', name='eliminarGasto'),
	url(r'^modificarGasto/', 'AdminConsorcios.views.modificarGasto', name='modificarGasto'),
	url(r'^modificarServicio/', 'AdminConsorcios.views.modificarServicio', name='modificarServicio'),
	url(r'^modificarAbono/', 'AdminConsorcios.views.modificarAbono', name='modificarAbono'),
	url(r'^agregarUnidadFuncional/', 'AdminConsorcios.views.agregarUnidadFuncional', name='agregarUnidadFuncional'),
	url(r'^aperturaCajaAdministracion/', 'AdminConsorcios.views.aperturaCajaAdministracion', name='aperturaCajaAdministracion'),
	url(r'^modificarCajaAdministracion/', 'AdminConsorcios.views.modificarCajaAdministracion', name='modificarCajaAdministracion'),
	url(r'^eliminarCajaAdministracion/', 'AdminConsorcios.views.eliminarCajaAdministracion', name='eliminarCajaAdministracion'),
	url(r'^mostrarCajaAdministracion/', 'AdminConsorcios.views.mostrarCajaAdministracion', name='mostrarCajaAdministracion'),
	url(r'^mostrarCajaConsorcio/', 'AdminConsorcios.views.mostrarCajaConsorcio', name='mostrarCajaConsorcio'),
	url(r'^eliminarCajaConsorcio/', 'AdminConsorcios.views.eliminarCajaConsorcio', name='eliminarCajaConsorcio'),
	url(r'^aperturaCajaConsorcio/', 'AdminConsorcios.views.aperturaCajaConsorcio', name='aperturaCajaConsorcio'),
	url(r'^modificarCajaConsorcio/', 'AdminConsorcios.views.modificarCajaConsorcio', name='modificarCajaConsorcio'),
	url(r'^mostrarAbono/', 'AdminConsorcios.views.mostrarAbono', name='mostrarAbono'),
	url(r'^mostrarGasto/', 'AdminConsorcios.views.mostrarGasto', name='mostrarGasto'),
	url(r'^mostrarServicio/', 'AdminConsorcios.views.mostrarServicio', name='mostrarServicio'),
	url(r'^agregarEmpleado/', 'AdminConsorcios.views.agregarEmpleado', name='agregarEmpleado'),
	url(r'^modificarEmpleado/(?P<id>\d+)/$', 'AdminConsorcios.views.modificarEmpleado', name='modificarEmpleado'),
	url(r'^eliminarEmpleado/', 'AdminConsorcios.views.eliminarEmpleado', name='eliminarEmpleado'),
	url(r'^modificarUnidadFuncional/(?P<id>\d+)/$', 'AdminConsorcios.views.modificarUnidadFuncional', name='modificarUnidadFuncional'),
	url(r'^archivarConsorcio/', 'AdminConsorcios.views.archivarConsorcio', name='archivarConsorcio'),
	url(r'^mostrarConsorcioArchivado/', 'AdminConsorcios.views.mostrarConsorcioArchivado', name='mostrarConsorcioArchivado'),
	url(r'^mostrarEstadisticas/', 'AdminConsorcios.views.mostrarEstadisticas', name='mostrarEstadisticas'),
	url(r'^arqueoCajas/', 'AdminConsorcios.views.arqueoCajas', name='arqueoCajas'),
	url(r'^api/get_consorcio/$', 'AdminConsorcios.views.get_consorcio', name='get_consorcio'),
	url(r'^lista_consorcio/$', 'AdminConsorcios.views.lista_consorcio', name='lista_consorcio'),  
	url(r'^ejemplo/', 'AdminConsorcios.views.ejemplo', name='ejemplo'),
	url(r'^archivarReclamo/', 'AdminConsorcios.views.archivarReclamo', name='archivarReclamo'),
	url(r'^mostrarReclamoArchivado/', 'AdminConsorcios.views.mostrarReclamoArchivado', name='mostrarReclamoArchivado'),
	url(r'^busquedaConsorcio/', 'AdminConsorcios.views.busquedaConsorcio', name='busquedaConsorcio'),
	url(r'^mostrarEmpleado/', 'AdminConsorcios.views.mostrarEmpleado', name='mostrarEmpleado'),
	url(r'^mostrarUnidadFuncional/', 'AdminConsorcios.views.mostrarUnidadFuncional', name='mostrarUnidadFuncional'),
	url(r'^mostrarFacturaArchivada/', 'AdminConsorcios.views.mostrarFacturaArchivada', name='mostrarFacturaArchivada'),
	url(r'^archivarFactura/', 'AdminConsorcios.views.archivarFactura', name='archivarFactura'),
	url(r'^agregarAlerta/', 'AdminConsorcios.views.agregarAlerta', name='agregarAlerta'),
	url(r'^modificarConsorcioDato/', 'AdminConsorcios.views.modificarConsorcioDato', name='modificarConsorcioDato'),
	url(r'^ingresarMuchasFacturas/', 'AdminConsorcios.views.ingresarMuchasFacturas', name='ingresarMuchasFacturas'),
	url(r'^usuario/perfil/', 'AdminConsorcios.views.perfil', name='perfil'),
	url(r'^usuario/modificarPerfil/', 'AdminConsorcios.views.modificarPerfil', name='modificarPerfil'),
	url(r'^mostrarAlerta/', 'AdminConsorcios.views.mostrarAlerta', name='mostrarAlerta'),	
	url(r'^eliminarAlerta/', 'AdminConsorcios.views.eliminarAlerta', name='eliminarAlerta'),	
	
	
	
	
	)
	
