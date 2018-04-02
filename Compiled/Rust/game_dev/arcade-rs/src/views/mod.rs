use phi::{Phi, ViewAction, View};
use phi::data::Rectangle;
use std::path::Path;
use sdl2::pixels::Color;
//use sdl2::render::{Texture, TextureQuality};
use sdl2_image::LoadTexture;

const PLAYER_SPEED: f64 = 180.0;
pub struct DefaultView;
struct YellowView;
struct GreenView;

struct Ship {
    rect: Rectangle
}

pub struct ShipView {
    player: Ship
}


impl ShipView {
    pub fn new(phi: &mut Phi) -> ShipView {
        ShipView {
            player: Ship {
                rect: Rectangle {
                    x: 128.0,
                    y: 128.0,
                    w: 64.0,
                    h: 64.0
                }
            }
        }
     }
}


impl View for YellowView {
    fn render(&mut self, context: &mut Phi, _: f64) -> ViewAction {
        if context.events.now.quit {
            return ViewAction::Quit;
        }

        else if context.events.now.key_space == Some(true) {
            return ViewAction::ChangeView(Box::new(GreenView))
        }

        context.renderer.set_draw_color(Color::RGB(212, 210, 0));
        context.renderer.clear();

        ViewAction::None
    }
}

impl View for GreenView {
    fn render(&mut self, context: &mut Phi, _: f64) -> ViewAction {
        if context.events.now.quit {
            return ViewAction::Quit;
        }

        else if context.events.now.key_space == Some(true) {
            return ViewAction::ChangeView(Box::new(YellowView))
        }
        context.renderer.set_draw_color(Color::RGB(10, 210, 30));
        context.renderer.clear();

        ViewAction::None
    }
}

impl View for DefaultView {
    fn render(&mut self, context: &mut Phi, _: f64) -> ViewAction {
        let renderer = &mut context.renderer;
        let events = &context.events;

        if events.now.quit || events.now.key_escape == Some(true) {
            return ViewAction::Quit;
        }

        else if context.events.now.key_space == Some(true) {
            return ViewAction::ChangeView(Box::new(YellowView))
        }

        renderer.set_draw_color(Color::RGB(0, 0, 0));
        renderer.clear();

        ViewAction::None
    }
}


impl View for ShipView {
    fn render(&mut self, phi: &mut Phi, elapsed: f64) -> ViewAction {

        if phi.events.now.quit || phi.events.now.key_escape == Some(true) {
            return ViewAction::Quit;
        }

        let diagonal =
            (phi.events.key_up ^ phi.events.key_down) &&
            (phi.events.key_left ^ phi.events.key_right);

        let moved =
            if diagonal {1.0 / 2.0f64.sqrt() }
            else { 1.0 } * PLAYER_SPEED * elapsed;

        let dx = match (phi.events.key_left, phi.events.key_right) {
            (true, true) | (false, false) => 0.0,
            (true, false) => -moved,
            (false, true) => moved
        };

        let dy = match (phi.events.key_up, phi.events.key_down) {
            (true, true) | (false, false) => 0.0,
            (true, false) => -moved,
            (false, true) => moved
        };

        let movable_region = Rectangle {
            x: 0.0,
            y: 0.0,
            w: phi.output_size().0 * 0.7,
            h: phi.output_size().1
        };

        self.player.rect = self.player.rect.move_inside(movable_region).unwrap();
        self.player.rect.x += dx;
        self.player.rect.y += dy;

        phi.renderer.set_draw_color(Color::RGB(0, 0, 0));
        phi.renderer.clear();

        phi.renderer.set_draw_color(Color::RGB(200, 200, 50));
        phi.renderer.fill_rect(self.player.rect.to_sdl().unwrap());

        ViewAction::None
    }
}
