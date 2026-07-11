package cl.duoc.msusuarios.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class UsuarioController {

    @GetMapping("/test")
    public String test() {
        return "FUNCIONA";
    }
}