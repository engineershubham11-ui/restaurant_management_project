<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scaler=1" />
    <title>homepage . starter styles</title>
    <style>
    *,*: :before, *: :after{box-sizing:border-box}
    html:focus-within{scroll-behavior:smooth}
    body,h1,h2,h3,h4,p,figure,blockquote,d1,dd{margin:0}
    img,picture,svg,video{display:block;max-width:100%}
    button,input,select,textarea{font:inherit}

    :root{

    --bg: #0f172a;
    --bg-soft: #111827;
    --surface: #111827;
    --text: #e5e7eb;
    --muted: #9ca3af;
    --brand: #22d3ee;
    --brand-ink: #0e7490;
    --accent: #0a78bfa;
    --ring: rgba(34,211,238,.45);
    --radius: 16px;
    --shadow: 0 10px 30px rgba(0,0,0,.25);


    --font-sans: ui-sans-serif, system-ui, -apple-system, segoe UI, roboto, "helvetica Neue", Arial, "Noto sans", "Apple color Emogi", "segoe UI Emoji";
    --fs-xs: .85rem;
    --fs-sm: .95rem;
    --fs-base: 1.05rem;
    --fs-lg: 1.25rem;
    --fs-xl: clamp(1.8rem,3vw + 1rem, 2.6rem);
    --fs-2xl: clamp(2.2rem, 5vw + 1rem, 3.2rem);
    --lh: 1.6;
    --space-1: .5rem;
    --space-2: .75rem;
    --space-3: 1rem;
    --space-4: 1.5rem;
    --space-6: 2rem;
    --space-8: 3rem;
    --content-w: min(100%, 1100px);

}

body{
    background: radial-gradient(1200px 600px at 10% -10%, rgba(167, 139, 250, .15 ), transparent 60%),
    radial-gradient(900px 500px at 120% 10%, rgba(34, 211, 238, .12), transparent 55%),
    var(--bg);
    color: var(--text);
    font-family: var(--font-sans);
    font-size: var(--fs-base);
    line-height: var(--lh);
    -webkit-font-smoothing: antialiased;
    -moz-oxs-font-smoothing: grayscale;
}