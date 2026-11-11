# Tips regarding UI/UX

- **Motion**

  - Material Design uses real-world metaphors as its foundation. Objects in the real world don't move linearly, they move in curved paths and accelerate and decelerate according to the motion's properties.
  - As such, motion should also use such properties and animate objects so that the motion feels natural rather than forced
  - For example, a car leaving the screen in a movie starts off slowly, then accelerates till it's out of the frame. Similarly, views should be interpolated using classes like AccelerateInterpolator, FastOutSlowInInterpolator, etc. [[More Info]](https://developer.android.com/reference/android/animation/TimeInterpolator.html)
  - When changing the visibilities of views, if you add `android:animateLayoutChanges="true"` to the parent, you get a nice little animation for free.

- **Typography**
  - While custom typefaces can be used for branding, it is essential to stick to Roboto and Noto if possible, especially for body text, due to their clarity and optimistic nature.
  - Roboto covers Latin, Greek and Cyrillic extended scripts, with Noto filling in for other language scripts [[More Info]](https://m2.material.io/design/typography.html#)
  - Weight balancing is an important aspect of typography, the fundamental concept of which is that the larger a typeface is, the less its weight should be so that it doesn't appear too thick and balances its weight with smaller typefaces of higher weights
  - Typography should align to a 4dp baseline grid, and maintain a minimum contrast ratio of 4.5:1 based on luminance values, with a recommended ratio being 7:1.
  - The ideal reading length for large blocks of text is 40 to 60 characters per line. Anything less is too narrow and anything more is too wide.

* **Icons**

  - Icons should be designed at 48dp, with 1dp edges, which equates to
    - 48px by 48px at mdpi
    - 72px by 72px at hdpi
    - 96px by 96px at xhdpi
    - 144px by 144px at xxhdpi
    - 192px by 192px at xxxhdpi
  - An additional icon of 512px by 512px should be designed for use on Google Play
  - Material icons, in addition to the base icon, should contain the following important elements
    - 1dp tinted edge at the top
    - 1dp shaded edge at the bottom
    - Contact shadow - a soft shadow around all edges of raised elements
    - Finish - a soft tint to provide surface lighting, fading from upper life to lower right [[More Info]](https://m2.material.io/design/iconography/product-icons.html)

* **Ripples**

  - When implementing Ripple Effect use `?attr/selectableItemBackground` instead of `?android:attr`
  - When implementing Ripples contained within the view like Button, use

    ```xml
    android:background="?attr/selectableItemBackground"
    ```

  - When implementing Ripples that extend beyond the view's bounds like ImageView:

    ```xml
    ?attr/selectableItemBackgroundBorderless
    ```

- **Other Points to Note**
  - Views should be aligned to Material Design's 8dp baseline grid and the keylines when possible. This gives the UI a sense of structure and hierarchy. [[More Info]](https://m2.material.io/design/layout/metrics-keylines.html)
  - If you plan on keeping a reference to any ViewGroup (LinearLayout, FrameLayout, RelativeLayout, etc.), and you don’t want to use any methods specific to this particular type of Layout, keep it as a ViewGroup object.
  - While picking an accent color (if the brand already has one), pick a color complementary to the primary color so that the contrast is high enough
