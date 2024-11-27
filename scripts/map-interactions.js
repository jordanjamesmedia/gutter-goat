document.addEventListener('DOMContentLoaded', () => {
    const mapPoints = document.querySelectorAll('.map-point');
    
    mapPoints.forEach(point => {
        const tooltip = point.querySelector('.map-tooltip');
        
        // Show tooltip on hover
        point.addEventListener('mouseenter', () => {
            tooltip.style.opacity = '1';
            
            // Position tooltip above point
            const pointRect = point.getBoundingClientRect();
            const tooltipRect = tooltip.getBoundingClientRect();
            
            tooltip.style.left = `${-tooltipRect.width/2 + pointRect.width/2}px`;
            tooltip.style.bottom = '20px';
        });
        
        // Hide tooltip
        point.addEventListener('mouseleave', () => {
            tooltip.style.opacity = '0';
        });
        
        // Click handler for navigation
        point.addEventListener('click', () => {
            const location = point.getAttribute('data-location').toLowerCase();
            window.location.href = `locations/${location}.html`;
        });
    });
    
    // Optional: Highlight point when scrolling to corresponding list item
    const areaLinks = document.querySelectorAll('.area-link');
    areaLinks.forEach(link => {
        link.addEventListener('mouseenter', () => {
            const location = link.textContent;
            const correspondingPoint = document.querySelector(`.map-point[data-location="${location}"]`);
            if (correspondingPoint) {
                correspondingPoint.style.transform = 'scale(1.2)';
            }
        });
        
        link.addEventListener('mouseleave', () => {
            const location = link.textContent;
            const correspondingPoint = document.querySelector(`.map-point[data-location="${location}"]`);
            if (correspondingPoint) {
                correspondingPoint.style.transform = 'scale(1)';
            }
        });
    });
}); 