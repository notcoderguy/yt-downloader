<?php

use App\Models\User;

test('registration screen can be rendered when no users exist', function () {
    $response = $this->get('/register');
    $response->assertStatus(200);
});

test('registration screen redirects when users exist', function () {
    User::factory()->create();

    $response = $this->get('/register');
    $response->assertRedirect('/login');
    $response->assertSessionHas('error', 'Registration is disabled');
});

test('new users can register when no users exist', function () {
    $response = $this->post('/register', [
        'name' => 'Test User',
        'email' => 'test@example.com',
        'password' => 'password',
        'password_confirmation' => 'password',
    ]);

    $this->assertAuthenticated();
    $response->assertRedirect(route('dashboard', absolute: false));
});

test('registration fails when users exist', function () {
    User::factory()->create();

    $response = $this->post('/register', [
        'name' => 'Test User',
        'email' => 'test@example.com',
        'password' => 'password',
        'password_confirmation' => 'password',
    ]);

    $response->assertRedirect();
    $response->assertSessionHasErrors(['error' => 'Registration is disabled']);
});
