<?php

use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('welcome');
});

#Auth::routes();

#Route::get('/home', 'HomeController@index')->name('home');

Route::get('/{any}','HomeController@vueroute')->where('any', '.*');

Route::get('/confinement','HomeController@vueroute')->name('confinement');
Route::get('/deconfinement','HomeController@vueroute')->name('deconfinement');
Route::get('/hybride','HomeController@vueroute')->name('hybride');
Route::get('/entrainer','HomeController@vueroute')->name('entrainer');
Route::get('/info','HomeController@vueroute')->name('info');




