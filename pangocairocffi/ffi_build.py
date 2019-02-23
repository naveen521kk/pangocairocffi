"""
    pangocairocffi.ffi_build
    ~~~~~~~~~~~~~~~~~~~

    Build the cffi bindings

"""

import sys
from pathlib import Path
from cffi import FFI
from pangocffi import ffi_build

sys.path.append(str(Path(__file__).parent))

# Create an empty _generated folder if needed
(Path(__file__).parent / '_generated').mkdir(exist_ok=True)

# cffi definitions, in the order outlined in https://developer.gnome.org/pango/stable/pango-Cairo-Rendering.html
ffi = FFI()
ffi.include(ffi_build.ffi)
ffi.set_source('pangocairocffi._generated.ffi', None)
ffi.cdef('''
    /* === GLib === */
    
    // typedef void* gpointer;
    typedef int gint;
    typedef int gboolean;
    typedef ... GDestroyNotify;
    void g_object_unref (gpointer object);
    
    /* === Cairo === */

    typedef void cairo_t;
    typedef void cairo_font_type_t;
    typedef void cairo_scaled_font_t;
    typedef void cairo_font_options_t;

    /* === Pango === */

    typedef ... PangoFontMap;
    typedef ... PangoCairoFontMap;
    // typedef ... PangoContext;
    typedef ... PangoCairoFont;
    typedef ... PangoAttrShape;
    // typedef ... PangoLayout;
    typedef ... PangoFont;
    typedef ... PangoGlyphString;
    typedef ... PangoGlyphItem;
    typedef ... PangoLayoutLine;
    typedef void (* PangoCairoShapeRendererFunc) (cairo_t *cr, PangoAttrShape *attr, gboolean do_path, gpointer data);
        
    PangoFontMap * pango_cairo_font_map_get_default (void);
    void pango_cairo_font_map_set_default (PangoCairoFontMap *fontmap);
    PangoFontMap * pango_cairo_font_map_new (void);
    PangoFontMap * pango_cairo_font_map_new_for_font_type (cairo_font_type_t fonttype);
    cairo_font_type_t pango_cairo_font_map_get_font_type (PangoCairoFontMap *fontmap);
    void pango_cairo_font_map_set_resolution (PangoCairoFontMap *fontmap, double dpi);
    double pango_cairo_font_map_get_resolution (PangoCairoFontMap *fontmap);
    PangoContext * pango_cairo_font_map_create_context (PangoCairoFontMap *fontmap);
    cairo_scaled_font_t * pango_cairo_font_get_scaled_font (PangoCairoFont *font);
    void pango_cairo_context_set_resolution (PangoContext *context, double dpi);
    double pango_cairo_context_get_resolution (PangoContext *context);
    void pango_cairo_context_set_font_options (PangoContext *context, const cairo_font_options_t *options);
    const cairo_font_options_t * pango_cairo_context_get_font_options (PangoContext *context);
    void pango_cairo_context_set_shape_renderer (
        PangoContext *context,
        PangoCairoShapeRendererFunc func,
        gpointer data,
        GDestroyNotify dnotify
    );
    PangoCairoShapeRendererFunc pango_cairo_context_get_shape_renderer (PangoContext *context, gpointer *data);
    PangoContext * pango_cairo_create_context (cairo_t *cr);
    void pango_cairo_update_context (cairo_t *cr, PangoContext *context);
    PangoLayout * pango_cairo_create_layout (cairo_t *cr);
    void pango_cairo_update_layout (cairo_t *cr, PangoLayout *layout);
    void pango_cairo_show_glyph_string (cairo_t *cr, PangoFont *font, PangoGlyphString *glyphs);
    void pango_cairo_show_glyph_item (cairo_t *cr, const char *text, PangoGlyphItem *glyph_item);
    void pango_cairo_show_layout_line (cairo_t *cr, PangoLayoutLine *line);
    void pango_cairo_show_layout (cairo_t *cr, PangoLayout *layout);
    void pango_cairo_show_error_underline (cairo_t *cr,double x, double y, double width, double height);
    void pango_cairo_glyph_string_path (cairo_t *cr, PangoFont *font, PangoGlyphString *glyphs);
    void pango_cairo_layout_line_path (cairo_t *cr, PangoLayoutLine *line);
    void pango_cairo_layout_path (cairo_t *cr, PangoLayout *layout);
    void pango_cairo_error_underline_path (cairo_t *cr, double x, double y, double width, double height);
''')

if __name__ == '__main__':
    ffi.compile()